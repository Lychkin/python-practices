def split_and_sort_numbers(*nums):
    positive_nums, negative_nums = [], []
    for num in nums:
        if num >= 0:
            positive_nums.append(num)
        else:
            negative_nums.append(num)

    return (sorted(negative_nums, reverse=True), sorted(positive_nums))


def main():
    print(split_and_sort_numbers(3, -1, 0, -5, 2, -2))
    print(split_and_sort_numbers(5, 1, 9, 2))
    print(split_and_sort_numbers(-7, -3, -10))
    print(split_and_sort_numbers(3.5, -2.1, 0.0, -7.7, 2.2))
    print(split_and_sort_numbers(0, 0, -1, -1, 2, 2))
    print(split_and_sort_numbers(-0.5, 0.5, -1.5, 1.5))
    print(split_and_sort_numbers(42))
    print(split_and_sort_numbers(-99))
    print(split_and_sort_numbers())


if __name__ == "__main__":
    main()
