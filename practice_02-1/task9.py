def main():
    word = "объектно-ориентированный"
    new_words = []
    new_words.extend(
        [word[0:6],
         word[9:17],
         word[14:17],
         word[4:15:5],
         word[10]+word[12:15]+word[19]])
    print(*new_words)


if __name__ == "__main__":
    main()
