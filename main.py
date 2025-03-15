import sys

from stats import get_num_words
from stats import get_character_count

def main():
    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")

    # book_text = get_book_text(path)
    # print(content)
    try:
        word_count = get_num_words(path)
        print(f"Found {word_count} total words")
    except Exception as e:
        print(f"ERROR: no valid file found in {path}, please try again")
        sys.exit(1)

    print("--------- Character Count -------")

    character_count = get_character_count(path)
    for character in character_count:
        print(f"{character["char"]}: {character["num"]}")


    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()