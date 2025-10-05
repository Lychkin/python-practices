def main():
    numbers = input("Введите вещественные числа через пробел: ")
    with open("examples/sample_result_task1.txt", "w") as file:
        file.write("\n".join(numbers.split()))


if __name__ == "__main__":
    main()
