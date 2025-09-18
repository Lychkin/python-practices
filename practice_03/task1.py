def encode(string, shift):
    encoded = []
    for char in string:
        if char.isalpha():
            if char.islower():
                encoded.append(chr((ord(char) + shift - 97) % 26 + 97))
            else:
                encoded.append(chr((ord(char) + shift - 65) % 26 + 65))
        else:
            encoded.append(char)
    return "".join(encoded)


def decode(string, shift):
    decoded = []
    for char in string:
        if char.isalpha():
            if char.islower():
                decoded.append(chr((ord(char) - shift - 97) % 26 + 97))
            else:
                decoded.append(chr((ord(char) - shift - 65) % 26 + 65))
        else:
            decoded.append(char)
    return "".join(decoded)


def main():
    print(encode("abc", 1))
    print(decode("bcd", 1))

    print(encode("xyz", 3))
    print(decode("abc", 3))

    print(encode("AbC", 2))
    print(decode("CdE", 2))

    print(encode("Hello, World!", 5))
    print(decode("Mjqqt, Btwqi!", 5))

    print(encode("Python", 0))
    print(decode("Python", 0))

    print(encode("abc", -1))
    print(decode("zab", -1))

    print(encode("abc", 29))
    print(decode("def", 29))


if __name__ == "__main__":
    main()
