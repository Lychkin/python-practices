import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QMessageBox,
    QMenu,
    QTableWidgetItem,
)
from PyQt5.QtCore import QPoint

from ui_main_window import Ui_MainWindow
from ui_add_book import Ui_AddBookDialog


class AddBookDialog(QDialog, Ui_AddBookDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.add_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_data(self):
        return (
            self.title_input.text(),
            self.author_input.text(),
            self.year_input.text(),
            self.genre_combo.currentText(),
        )


class LibraryApp(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.books = []

        self.add_button.clicked.connect(self.add_book)
        self.genre_filter.currentTextChanged.connect(self.apply_filter)
        self.table.customContextMenuRequested.connect(self.show_context_menu)

    def add_book(self):
        dialog = AddBookDialog(self)
        if dialog.exec_():
            title, author, year, genre = dialog.get_data()

            if not title or not author or not year:
                QMessageBox.warning(
                    self, "Ошибка", "Пожалуйста, заполните все поля!"
                )
                return

            self.books.append(
                {
                    "Название": title,
                    "Автор": author,
                    "Год издания": year,
                    "Жанр": genre,
                }
            )
            self.update_table()

    def update_table(self):
        genre_filter = self.genre_filter.currentText()
        if genre_filter == "Все":
            filtered_books = self.books
        else:
            filtered_books = [
                b for b in self.books if b["Жанр"] == genre_filter
            ]

        self.table.setRowCount(0)
        for book in filtered_books:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(book["Название"]))
            self.table.setItem(row, 1, QTableWidgetItem(book["Автор"]))
            self.table.setItem(row, 2, QTableWidgetItem(book["Год издания"]))
            self.table.setItem(row, 3, QTableWidgetItem(book["Жанр"]))

    def apply_filter(self):
        self.update_table()

    def show_context_menu(self, pos: QPoint):
        menu = QMenu()
        delete_action = menu.addAction("Удалить книгу")
        action = menu.exec_(self.table.viewport().mapToGlobal(pos))
        if action == delete_action:
            self.delete_book()

    def delete_book(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.information(
                self, "Удаление", "Выберите книгу для удаления."
            )
            return

        reply = QMessageBox.question(
            self,
            "Подтверждение удаления",
            "Удалить выбранную книгу?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            for index in sorted(selected_rows, reverse=True):
                row_data = [
                    self.table.item(index.row(), col).text() for col in range(4)
                ]
                self.books = [
                    b
                    for b in self.books
                    if not (
                        b["Название"] == row_data[0]
                        and b["Автор"] == row_data[1]
                        and b["Жанр"] == row_data[3]
                    )
                ]
            self.update_table()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryApp()
    window.show()
    sys.exit(app.exec_())
