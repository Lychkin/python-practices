import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QFileDialog,
    QToolBar,
    QAction,
    QMessageBox,
)
from PyQt5.QtGui import QFont


class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Текстовый редактор")
        self.setGeometry(200, 200, 800, 600)

        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont("Consolas", 12))
        self.setCentralWidget(self.text_edit)

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        bold_action = QAction("Жирный", self)
        bold_action.setShortcut("Ctrl+B")
        bold_action.triggered.connect(self.toggle_bold)
        toolbar.addAction(bold_action)

        toolbar.addSeparator()

        undo_action = QAction("Отменить", self)
        undo_action.setShortcut("Ctrl+Z")
        undo_action.triggered.connect(self.text_edit.undo)
        toolbar.addAction(undo_action)

        redo_action = QAction("Повторить", self)
        redo_action.setShortcut("Ctrl+Y")
        redo_action.triggered.connect(self.text_edit.redo)
        toolbar.addAction(redo_action)

        toolbar.addSeparator()

        save_action = QAction("Сохранить", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_file)
        toolbar.addAction(save_action)

        open_action = QAction("Загрузить", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.load_file)
        toolbar.addAction(open_action)

    def toggle_bold(self):
        fmt = self.text_edit.currentCharFormat()
        if fmt.fontWeight() == QFont.Bold:
            fmt.setFontWeight(QFont.Normal)
        else:
            fmt.setFontWeight(QFont.Bold)
        self.text_edit.setCurrentCharFormat(fmt)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Сохранить файл", "", "Текстовые файлы (*.txt)"
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(self.text_edit.toPlainText())
            except Exception as e:
                QMessageBox.warning(
                    self, "Ошибка", f"Не удалось сохранить файл:\n{e}"
                )

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Открыть файл", "", "Текстовые файлы (*.txt)"
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.text_edit.setPlainText(file.read())
            except Exception as e:
                QMessageBox.warning(
                    self, "Ошибка", f"Не удалось загрузить файл:\n{e}"
                )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec_())
