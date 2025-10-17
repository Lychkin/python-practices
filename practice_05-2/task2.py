import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QComboBox, QListWidget,
    QListWidgetItem, QMessageBox, QLabel
)
from PyQt5.QtGui import QIcon


class RecipeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Каталог рецептов")
        self.setGeometry(100, 100, 400, 400)

        self.recipes = {
            "Завтрак": {
                "Омлет": ["яйца", "молоко", "соль"],
                "Каша овсяная": ["овсянка", "молоко"]
            },
            "Обед": {
                "Борщ": ["свёкла", "мясо", "капуста"]
            },
            "Ужин": {
                "Паста с сыром": ["макароны", "сыр", "сливки"]
            }
        }

        self.favorites = set()

        self.layout = QVBoxLayout()
        self.combo = QComboBox()
        self.list_widget = QListWidget()
        self.status_label = QLabel("Выберите категорию блюд")

        self.combo.addItems(self.recipes.keys())
        self.combo.currentTextChanged.connect(self.update_list)

        self.list_widget.itemDoubleClicked.connect(self.show_ingredients)
        self.list_widget.itemClicked.connect(self.toggle_favorite)

        self.layout.addWidget(self.combo)
        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.status_label)
        self.setLayout(self.layout)

        self.update_list(self.combo.currentText())

    def update_list(self, category):
        self.list_widget.clear()
        for dish in self.recipes[category]:
            item = QListWidgetItem(dish)
            if dish in self.favorites:
                item.setIcon(QIcon.fromTheme("starred", QIcon("⭐")))
            else:
                item.setIcon(QIcon.fromTheme("unstarred", QIcon("☆")))
            self.list_widget.addItem(item)
        self.status_label.setText(f"Выбрана категория: {category}")

    def show_ingredients(self, item):
        category = self.combo.currentText()
        dish_name = item.text()
        ingredients = self.recipes[category].get(dish_name, [])
        text = "\n".join(ingredients)
        QMessageBox.information(self, dish_name, f"Ингредиенты:\n{text}")

    def toggle_favorite(self, item):
        dish_name = item.text()
        if dish_name in self.favorites:
            self.favorites.remove(dish_name)
            item.setIcon(QIcon.fromTheme("unstarred", QIcon("☆")))
        else:
            self.favorites.add(dish_name)
            item.setIcon(QIcon.fromTheme("starred", QIcon("⭐")))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RecipeApp()
    window.show()
    sys.exit(app.exec_())
