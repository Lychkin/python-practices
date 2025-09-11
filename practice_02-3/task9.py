def multiplication_table(n):
    print('-' * 50)
    for num1 in range(1, n+1):
        for num2 in range(1, n+1):
            print(f"{num1} x {num2} = {num1*num2}", end='\t')
        print()


def main():
    multiplication_table(9)
    multiplication_table(3)
    multiplication_table(5)


if __name__ == "__main__":
    main()
