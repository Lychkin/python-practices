class Roman:
    roman_map = (
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    )

    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
            self.roman = self.int_to_roman(value)
        elif isinstance(value, str):
            self.roman = value
            self.value = self.roman_to_int(value)

    def __str__(self):
        return self.roman

    def __repr__(self):
        return f"Roman('{self.roman}') {self.value}"

    def __add__(self, other):
        return Roman(self.value + other.value)

    def __sub__(self, other):
        return Roman(self.value - other.value)

    def __mul__(self, other):
        return Roman(self.value * other.value)

    def __truediv__(self, other):
        return Roman(self.value // other.value)

    @staticmethod
    def int_to_roman(num):
        result = ""
        for symbol, val in Roman.roman_map:
            while num >= val:
                result += symbol
                num -= val
        return result

    @staticmethod
    def roman_to_int(s):
        i, result = 0, 0
        for symbol, val in Roman.roman_map:
            while s[i: i + len(symbol)] == symbol:
                result += val
                i += len(symbol)
        return result


def main():
    a = Roman("CDXI")
    b = Roman(15)
    number = a + b
    print(number, number.value)
    number = a - b
    print(number, number.value)
    number = a * b
    print(number, number.value)
    number = a / b
    print(number, number.value)


if __name__ == "__main__":
    main()
