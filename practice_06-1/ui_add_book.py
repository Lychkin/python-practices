from PyQt5.QtWidgets import (
    QDialog,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QPushButton,
    QHBoxLayout,
)
from PyQt5.QtGui import QIntValidator


class Ui_AddBookDialog(object):
    def setupUi(self, Dialog: QDialog):
        Dialog.setWindowTitle("Добавить книгу")
        Dialog.resize(600, 200)

        self.layout = QFormLayout(Dialog)

        self.title_input = QLineEdit()
        self.author_input = QLineEdit()
        self.year_input = QLineEdit()
        self.year_input.setValidator(QIntValidator(0, 9999))
        self.genre_combo = QComboBox()
        self.genre_combo.addItems(
            ["Роман", "Фантастика", "Детектив", "Поэзия", "Научная литература"]
        )

        self.layout.addRow("Название:", self.title_input)
        self.layout.addRow("Автор:", self.author_input)
        self.layout.addRow("Год издания:", self.year_input)
        self.layout.addRow("Жанр:", self.genre_combo)

        self.add_button = QPushButton("Добавить")
        self.cancel_button = QPushButton("Отмена")
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.cancel_button)
        self.layout.addRow(self.button_layout)
