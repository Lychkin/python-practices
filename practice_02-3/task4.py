def last_digit(n):
    return int(str(n)[-1])


def interesting_nums(k, s, start):
    nums_count = 0
    current_num = start+1
    while (nums_count != 10):
        if (last_digit(current_num) == k) and (current_num % s == 0):
            print(current_num, end=' ')
            nums_count += 1
        current_num += 1
    print()


def main():
    interesting_nums(2, 8, 10)
    interesting_nums(5, 3, -10)
    interesting_nums(0, 5, 5)
    interesting_nums(7, 7, 0)
    interesting_nums(5, 1, -10)
    interesting_nums(2, 1, 1000)


if __name__ == "__main__":
    main()
