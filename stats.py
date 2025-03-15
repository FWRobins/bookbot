def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(path_to_file):
    content = get_book_text(path_to_file)
    words_list = content.split()
    word_count = len(words_list)
    return word_count

def get_character_count(path_to_file):
    content = get_book_text(path_to_file)
    content = content.lower()
    character_dict = {}
    for character in content:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            # count = character_dict[character]
            character_dict[character] = character_dict[character] +1
    return character_dict