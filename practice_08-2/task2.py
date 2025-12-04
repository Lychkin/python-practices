import os
from copy import copy
import sqlite3
from datetime import datetime, date
from colorama import init as colorama_init
from colorama import Fore, Style
from tabulate import tabulate


class TaskManager:
    def __init__(self):
        self.connection = sqlite3.connect("tasks.db")
        self.cursor = self.connection.cursor()
        self.options = [
            "1. Сортировать задачи по",
            "2. Добавить задачу",
            "3. Отметить выполненной",
            "4. Удалить задачу",
            "5. Показать просроченные",
            "6. Поиск по тексту",
            "7. Удалить все задачи",
            "8. Выйти",
        ]
        self.create_db()
        TaskManager.overdues = False
        TaskManager.sort_by_options = ["id", "дедлайну", "приоритету"]
        TaskManager.current_sort_by = TaskManager.sort_by_options[0]

    def clear_last_line(self, times=1):
        # Очистить предыдущую строку (ту, где был ввод)
        for _ in range(times):
            print("\033[F\033[K", end="")

    def run(self):
        while True:
            os.system("cls")
            self.get_tasks()
            self.show_statistics()
            self.show_tasks()
            self.show_options()
            print()
            user_action = int(input())
            self.clear_last_line()

            if user_action == 1:
                self.change_sorting()
            elif user_action == 2:
                self.add_task()
            elif user_action == 3:
                self.complete_task()
            elif user_action == 4:
                self.delete_task()
            elif user_action == 5:
                self.show_overdues()
            elif user_action == 6:
                self.search()
            elif user_action == 7:
                self.delete_all_tasks()
            elif user_action == 8:
                self.connection.close()
                break
            else:
                pass

    def get_headers(self):
        headers = [
            Style.BRIGHT + "id",
            Style.BRIGHT + "Текст задачи",
            Style.BRIGHT + "Дедлайн",
            Style.BRIGHT + "Приоритет",
            Style.BRIGHT + "Выполнена",
            Style.BRIGHT + "Создана" + Style.RESET_ALL,
        ]
        if TaskManager.current_sort_by == "id":
            headers[0] = Fore.LIGHTBLUE_EX + headers[0] + Fore.RESET
        if TaskManager.current_sort_by == "дедлайну":
            headers[2] = Fore.LIGHTBLUE_EX + headers[2] + Fore.RESET
        if TaskManager.current_sort_by == "приоритету":
            headers[3] = Fore.LIGHTBLUE_EX + headers[3] + Fore.RESET
        return headers

    def check_row(self, id):
        for task in self.tasks:
            if task[0] == id:
                return True
        return False

    def create_db(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                deadline DATE,
                priority TEXT CHECK(priority IN ('высокий','средний','низкий')) DEFAULT 'средний',
                completed BOOLEAN DEFAULT 0,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        self.connection.commit()

    def get_tasks(self):
        self.cursor.execute(
            """
            SELECT *
            FROM tasks
            """
        )

        raw_tasks = self.cursor.fetchall()
        self.tasks = []

        self.connection.commit()

        for raw_task in raw_tasks:
            task = []
            task.append(raw_task[0])
            task.append(raw_task[1])
            if isinstance(raw_task[2], str):
                task.append(datetime.strptime(raw_task[2], "%Y-%m-%d").date())
            else:
                task.append(None)
            task.append(raw_task[3])
            task.append(raw_task[4])
            task.append(raw_task[5])
            self.tasks.append(task)

    def show_tasks(self):
        if TaskManager.current_sort_by == "дедлайну":
            sorted_tasks = sorted(
                self.tasks, key=lambda task: (task[2] is None, task[2])
            )
        elif TaskManager.current_sort_by == "приоритету":
            order = {"низкий": 0, "средний": 1, "высокий": 2}
            sorted_tasks = sorted(self.tasks, key=lambda task: order[task[3]])
        else:
            sorted_tasks = sorted(self.tasks, key=lambda task: task[0])

        self.formatted_tasks = []
        if TaskManager.overdues:
            for task in sorted_tasks:
                if task[2] is not None and (
                    task[2] < date.today() and task[4] == 0
                ):
                    self.formatted_tasks.append(
                        [
                            Fore.RED + str(field) + Style.RESET_ALL
                            for field in task
                        ]
                    )
                else:
                    self.formatted_tasks.append(task)
        else:
            self.formatted_tasks = copy(sorted_tasks)

        print(
            tabulate(
                self.formatted_tasks,
                headers=self.get_headers(),
                tablefmt="pretty"
            )
        )

    def search(self):
        while True:
            search_query = input(
                "Введите запрос - текст задачи: "
            ).strip()
            self.clear_last_line()
            if len(search_query) != 0:
                break

        search_result_tasks = list(
            filter(
                lambda task: search_query.lower() in task[1].lower(),
                self.formatted_tasks,
            )
        )
        print(
            Style.BRIGHT
            + f"Задачи по запросу `{search_query}`:"
            + Style.RESET_ALL
        )
        if len(search_result_tasks):
            print(
                tabulate(
                    search_result_tasks,
                    headers=self.get_headers(),
                    tablefmt="pretty",
                )
            )
        else:
            print("Ничего не найдено")
        while True:
            input("Нажмите Enter, чтобы продолжить")
            break

    def show_statistics(self):
        completed_tasks = list(
            filter(
                lambda task: task[4] == 1,
                self.tasks,
            )
        )
        ovedue_tasks = list(
            filter(
                lambda task: task[2] is not None
                and (task[2] < date.today() and task[4] == 0),
                self.tasks,
            )
        )
        statistics = {
            "Всего задач": len(self.tasks),
            "Выполнено": len(completed_tasks),
            "Просрочено": len(ovedue_tasks),
        }
        print(" | ".join(f"{key}: {val}" for key, val in statistics.items()))

    def show_options(self):
        print(
            self.options[0],
            Fore.LIGHTBLUE_EX + TaskManager.current_sort_by + Style.RESET_ALL,
            end=" | ",
        )
        print(self.options[1], end=" | ")
        print(self.options[2], end=" | ")
        print(self.options[3])
        print(self.options[4], end=" | ")
        print(self.options[5], end=" | ")
        print(self.options[6], end=" | ")
        print(self.options[7])

    def add_task(self):
        query_data = {}

        while True:
            text = input(
                "Введите текст задачи (обязательный параметр): "
            ).strip()
            self.clear_last_line()
            if len(text) != 0:
                query_data["text"] = text
                break

        while True:
            deadline = input(
                """Введите дедлайн задачи в формате день.месяц.год
                (чтобы пропустить, нажмите Enter): """
            ).strip()
            self.clear_last_line(2)
            if len(deadline) == 0:
                break
            try:
                deadline = str(datetime.strptime(deadline, "%d.%m.%Y").date())
                query_data["deadline"] = deadline
                break
            except ValueError:
                pass

        while True:
            priority = input(
                """Введите приоритет задачи - низкий, высокий или средний
                (чтобы пропустить, нажмите Enter): """
            ).strip()
            self.clear_last_line(2)
            if len(priority) == 0:
                break
            if (len(priority) != 0) and (
                priority in ["высокий", "средний", "низкий"]
            ):
                query_data["priority"] = priority
                break

        columns = ", ".join(query_data.keys())
        placeholders = ", ".join(["?"] * len(query_data))
        values = tuple(query_data.values())

        self.cursor.execute(
            f"""
            INSERT INTO tasks ({columns})
            VALUES ({placeholders});
            """,
            values,
        )

        self.connection.commit()

    def complete_task(self):
        while True:
            try:
                id = int(
                    input(
                        "Введите id задачи которую отметить выполненной: "
                    ).strip()
                )
                self.clear_last_line()
                if self.check_row(id):
                    break
                print("! Некорректные данные !")
            except ValueError:
                print("! Некорректные данные !")

        self.cursor.execute(
            """
            UPDATE tasks
            SET completed = 1
            WHERE id = ?;
            """,
            (id,),
        )

        self.connection.commit()

    def delete_task(self):
        while True:
            try:
                id = int(
                    input("Введите id задачи которую нужно удалить: ").strip()
                )
                self.clear_last_line()
                if self.check_row(id):
                    break
                print("! Некорректные данные !")
            except ValueError:
                print("! Некорректные данные !")

        self.cursor.execute(
            """
            DELETE FROM tasks
            WHERE id = ?;
            """,
            (id,),
        )

        self.connection.commit()

    def delete_all_tasks(self):
        self.cursor.execute(
            """
            DELETE FROM tasks;
            """
        )
        self.cursor.execute(
            """
            DELETE FROM sqlite_sequence WHERE name='tasks'
            """
        )

        self.connection.commit()

    def show_overdues(self):
        TaskManager.overdues = not TaskManager.overdues

    def change_sorting(self):
        next_index = (
            TaskManager.sort_by_options.index(TaskManager.current_sort_by) + 1
        ) % len(TaskManager.sort_by_options)
        TaskManager.current_sort_by = TaskManager.sort_by_options[next_index]


def main():
    colorama_init(autoreset=True)
    app = TaskManager()
    app.run()


if __name__ == "__main__":
    main()
