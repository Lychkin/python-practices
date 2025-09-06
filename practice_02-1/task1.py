
def nums_actions(n1, n2):
    print(f"{n1} + {n2} = {n1 + n2}")
    print(f"{n1} - {n2} = {n1 - n2}")
    print(f"{n1} * {n2} = {n1 * n2}")
    print(f"{n1} / {n2} = {round(n1 / n2, 2)}")
    print(f"{n1} // {n2} = {n1 // n2}")
    print(f"{n1} % {n2} = {n1 % n2}")
    print(f"{n1} < {n2} : {n1 < n2}")
    print(f"{n1} <= {n2} : {n1 <= n2}")
    print(f"{n1} > {n2} : {n1 > n2}")
    print(f"{n1} >= {n2} : {n1 >= n2}")
    print(f"{n1} != {n2} : {n1 != n2}")
    print(f"{n1} == {n2} : {n1 == n2}")


def main():
    a, b = map(int, input("Введите два целых числа через пробел:").split(' '))
    nums_actions(a, b)


if __name__ == "__main__":
    main()
