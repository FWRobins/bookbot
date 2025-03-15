from stats import get_num_words
# from stats import get_book_text

def main():
    # book_text = get_book_text("./books/frankenstein.txt")
    # print(content)

    word_count = get_num_words("./books/frankenstein.txt")
    print(f"{word_count} words found in the document")


main()