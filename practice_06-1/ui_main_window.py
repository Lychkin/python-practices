from PyQt5.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QComboBox,
    QLabel,
    QTableWidget,
    QHeaderView,
)
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Учёт книг в библиотеке")
        MainWindow.resize(1280, 720)

        self.main_layout = QHBoxLayout(MainWindow)

        self.left_layout = QVBoxLayout()
        self.add_button = QPushButton("Добавить книгу")
        self.left_layout.addWidget(self.add_button)
        self.filter_label = QLabel("Фильтр по жанру:")
        self.left_layout.addWidget(self.filter_label)

        self.genre_filter = QComboBox()
        self.genre_filter.addItems(
            [
                "Все",
                "Роман",
                "Фантастика",
                "Детектив",
                "Поэзия",
                "Научная литература",
            ]
        )
        self.left_layout.addWidget(self.genre_filter)

        self.left_layout.addStretch()
        self.main_layout.addLayout(self.left_layout, 1)

        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(
            ["Название", "Автор", "Год издания", "Жанр"]
        )
        self.table.setSelectionBehavior(self.table.SelectRows)
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.main_layout.addWidget(self.table, 4)
