def info(db):
    print("Список продуктов в магазине:\n")
    for product in db:
        print(f"{product['name']}")
        print(f" - ID: {product['id']}")
        print(f" - Цена: {product['price']}")
        print(f" - Кол-во: {product['quantity']}")
        print(f" - Масса: {product['weight']}")
        print(" - Состав:")
        print(f"\tбелки: {product['composition']['proteins']}")
        print(f"\tжиры: {product['composition']['fats']}")
        print(f"\tуглеводы: {product['composition']['carbs']}")
        print(f"\tкалории: {product['composition']['calories']}")
        print(f" - Категории: {product['categories']}")
        print(f" - Органический: {'Да' if product['is_organic'] else 'Нет'}")
        print("-" * 50)


def main():
    products_db = [
        {
            "id": 247,
            "name": "Йогурт натуральный",
            "price": 89.99,
            "quantity": 45,
            "weight": 150.5,
            "composition": {
                "proteins": 4.5,
                "fats": 2.0,
                "carbs": 6.0,
                "calories": 65
            },
            "categories": ["Молочные продукты", "Охлажденные товары"],
            "is_organic": True
        },
        {
            "id": 934,
            "name": "Хлеб 'Бородинский'",
            "price": 56.50,
            "quantity": 22,
            "weight": 500.0,
            "composition": {
                "proteins": 7.9,
                "fats": 1.0,
                "carbs": 42.3,
                "calories": 210
            },
            "categories": ["Хлебобулочные изделия", "Выпечка"],
            "is_organic": True
        },
        {
            "id": 571,
            "name": "Сок яблочный",
            "price": 120.00,
            "quantity": 38,
            "weight": 1000.0,
            "composition": {
                "proteins": 0.4,
                "fats": 0.1,
                "carbs": 11.5,
                "calories": 48
            },
            "categories": ["Соки", "Напитки", "Бакалея"],
            "is_organic": False
        }
    ]

    info(products_db)


if __name__ == "__main__":
    main()
