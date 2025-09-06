def f(x, y, z):
    return round(
        (((x**5+7)/(abs(-6)*y))**(1/3))/(7 - z % y),
        3)


def main():
    x, y, z = map(int, input("Введите значения x, y, z через пробел:").
                  split(' '))
    print(f(x, y, z))


if __name__ == "__main__":
    main()
