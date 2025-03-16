from collections import Counter

def txt_read_and_write ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def split_text():
    s_text = txt_read_and_write().split()
    return s_text

def char_count():
    c_text = txt_read_and_write().lower()
    char_dict = dict(Counter(c_text))
    return char_dict

def sort_on(char_dict):
    sorted_char_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_char_dict


def display_output():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    total_words = len(split_text())
    print(f"Found {total_words} total words")

    print("--------- Character Count -------")
    char_dict = char_count()
    sorted_characters = sort_on(char_dict)

    for char, count in sorted_characters:
        if char.strip():  # Exclude whitespace characters
            print(f"{char}: {count}")

    print("============= END ===============")










