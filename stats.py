def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(path_to_file):
    content = get_book_text(path_to_file)
    words_list = content.split()
    word_count = len(words_list)
    return word_count