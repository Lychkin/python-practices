def count_letters(text):
    words = text.lower().split()
    clean_words = []
    punctuation = ".,!?;:-—()\"'«»"
    for word in words:
        clean_word = word.strip(punctuation)
        if clean_word:
            clean_words.append(clean_word)
    vowels = "аеёиоуыэюя"
    vowel_counter = 0
    consonant_counter = 0
    for word in clean_words:
        if word[0] in vowels:
            vowel_counter += 1
        elif word[0].isalpha():
            consonant_counter += 1
    return (vowel_counter, consonant_counter)


def main():
    with open("data/input_for_task2.txt", encoding="utf-8") as file:
        poem_text = file.read()
        print(poem_text, "\n")
        letters = count_letters(poem_text)
        if letters[0] > letters[1]:
            print(f"Слов на гласную больше: {letters[0]} > {letters[1]}")
        elif letters[0] < letters[1]:
            print(f"Слов на согласную больше: {letters[0]} < {letters[1]}")
        else:
            print(f"Слов одинаково: {letters[0]} = {letters[1]}")


if __name__ == "__main__":
    main()
