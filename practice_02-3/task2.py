def quadratic_equation(a, b, c):
    discriminant = b*b - 4*a*c
    solution = []
    if discriminant > 0:
        solution.append(round((-b+discriminant**(0.5))/(2*a), 2))
        solution.append(round((-b-discriminant**(0.5))/(2*a), 2))
    if discriminant == 0:
        solution.append(round(-b/(2*a), 2))
    return solution


def main():
    print(quadratic_equation(1, 5, 6))
    print(quadratic_equation(1, -7, 10))
    print(quadratic_equation(3, 5, 2))
    print(quadratic_equation(2, -5, 3))
    print(quadratic_equation(5, 3, 0))
    print(quadratic_equation(1, -6, 9))
    print(quadratic_equation(13, -4, 6))


if __name__ == "__main__":
    main()
