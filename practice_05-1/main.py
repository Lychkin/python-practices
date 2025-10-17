import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QLabel,
    QGridLayout,
)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.first_num_label = QLabel("Первое число:")
        self.first_num_input = QLineEdit()
        self.second_num_label = QLabel("Второе число:")
        self.second_num_input = QLineEdit()

        self.result_label = QLabel("Результат:")
        self.result_output = QLineEdit()
        self.result_output.setReadOnly(True)

        self.btn_add = QPushButton("+")
        self.btn_sub = QPushButton("-")
        self.btn_mul = QPushButton("*")
        self.btn_div = QPushButton("/")
        self.btn_int_div = QPushButton("//")
        self.btn_mod = QPushButton("%")

        self.btn_add.clicked.connect(lambda: self.make_operation("+"))
        self.btn_sub.clicked.connect(lambda: self.make_operation("-"))
        self.btn_mul.clicked.connect(lambda: self.make_operation("*"))
        self.btn_div.clicked.connect(lambda: self.make_operation("/"))
        self.btn_int_div.clicked.connect(lambda: self.make_operation("//"))
        self.btn_mod.clicked.connect(lambda: self.make_operation("%"))

        layout = QGridLayout()
        layout.addWidget(self.first_num_label, 0, 0)
        layout.addWidget(self.first_num_input, 0, 1)
        layout.addWidget(self.second_num_label, 1, 0)
        layout.addWidget(self.second_num_input, 1, 1)

        layout.addWidget(self.btn_add, 2, 0)
        layout.addWidget(self.btn_sub, 2, 1)
        layout.addWidget(self.btn_mul, 2, 2)
        layout.addWidget(self.btn_div, 3, 0)
        layout.addWidget(self.btn_int_div, 3, 1)
        layout.addWidget(self.btn_mod, 3, 2)

        layout.addWidget(self.result_label, 4, 0)
        layout.addWidget(self.result_output, 4, 1, 1, 2)

        self.setLayout(layout)
        self.resize(300, 200)
        self.setWindowTitle("Мини-калькулятор")

    def make_operation(self, operation):
        try:
            num1 = float(self.first_num_input.text())
            num2 = float(self.second_num_input.text())

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2
            elif operation == "//":
                result = num1 // num2
            elif operation == "%":
                result = num1 % num2

            self.result_output.setText(str(result))
        except Exception:
            self.result_output.setText("Ошибка")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
