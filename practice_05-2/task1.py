import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QComboBox,
    QListWidget,
    QMessageBox,
    QLabel,
)


class TaskViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Список задач")
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Выберите категорию задач:")
        layout.addWidget(self.label)

        self.category_box = QComboBox()
        self.category_box.addItems(["Все", "Работа", "Учёба", "Личное"])
        layout.addWidget(self.category_box)

        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        self.setLayout(layout)

        self.tasks = [
            {
                "title": "Подготовить отчёт",
                "category": "Работа",
                "desc": "Сделать финансовый отчёт за октябрь.",
            },
            {
                "title": "Выучить PyQt5",
                "category": "Учёба",
                "desc": "Пройти курс по созданию GUI на PyQt5.",
            },
            {
                "title": "Купить продукты",
                "category": "Личное",
                "desc": "Молоко, хлеб, сыр, овощи.",
            },
            {
                "title": "Встреча с клиентом",
                "category": "Работа",
                "desc": "Обсудить новый проект с клиентом.",
            },
            {
                "title": "Подготовиться к экзамену",
                "category": "Учёба",
                "desc": "Повторить темы из последней лекции.",
            },
        ]

        # Заполняем список задач
        self.update_task_list(" ")

        # Подключаем сигналы
        self.category_box.currentTextChanged.connect(self.update_task_list)
        self.task_list.itemDoubleClicked.connect(self.show_task_description)

    def update_task_list(self, category):
        self.task_list.clear()
        for task in self.tasks:
            if category == "Все" or task["category"] == category:
                self.task_list.addItem(task["title"])

    def show_task_description(self, item):
        task_title = item.text()
        for task in self.tasks:
            if task["title"] == task_title:
                QMessageBox.information(self, task["title"], task["desc"])
                break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskViewer()
    window.show()
    sys.exit(app.exec_())
