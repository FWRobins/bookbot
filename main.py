# from stats import get_book_text
from stats import get_num_words
from stats import get_character_count

def main():
    path = "./books/frankenstein.txt"
    # book_text = get_book_text(path)
    # print(content)

    word_count = get_num_words(path)
    print(f"{word_count} words found in the document")

    character_count = get_character_count(path)
    print(character_count)
    # for key, value in character_count.items():
    #     print(f"{key}: {value}")


main()