def get_through_window(a, b, d):
    gap = 1
    if a >= d+gap*2 and b >= d+gap*2:
        return True
    else:
        return False


def main():
    print(get_through_window(10, 10, 15))
    print(get_through_window(15, 17, 15))
    print(get_through_window(20, 16, 15))
    print(get_through_window(17, 16, 15))
    print(get_through_window(17, 16, 15))
    print(get_through_window(17, 17, 15))
    print(get_through_window(20, 17, 15))
    print(get_through_window(20, 20, 15))


if __name__ == "__main__":
    main()
