import romanify


def roman_and_arabic(number):
    return f"Roman: {romanify.arabic2roman(number)} | Arabic: {number}"


def main():
    first_number = 32
    second_number = "MV"
    result = first_number + romanify.roman2arabic(second_number)
    print(roman_and_arabic(result))
    result = first_number - romanify.roman2arabic(second_number)
    print(roman_and_arabic(result))
    result = first_number * romanify.roman2arabic(second_number)
    print(roman_and_arabic(result))
    result = first_number / romanify.roman2arabic(second_number)
    print(roman_and_arabic(result))


if __name__ == "__main__":
    main()
