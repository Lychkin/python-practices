from math import prod


def num_actions(num):
    a = list(map(int, list(str(num))))
    print(f"Сумма цифр {num}: {sum(a)}")
    print(f"Произведение цифр {num}: {prod(a)}")


def main():
    a = 74
    b = 351
    num_actions(a)
    num_actions(b)


if __name__ == "__main__":
    main()
