from collections import Counter
import tkinter as tk
from tkinter import filedialog

files_ending = 0
header_printed = False
results = []


"""""

The FUNCTIONS under this TEXT was made for jOkINg way of algorithms practice (THAT COOL BUT THE WAY IT WAS MADE AND FOR WHAT - IS CRUEL, who need this?)

So anyway i'd like to add an more useful function in future like sMaRT tEXt rEaDInG EmPOweRed with AI

But tbh its probably will be in not in few weeks

At the moment of March 16th I started to work on simple "Text Search System" that could not just find words (who need this?), but also tacking a part of the text 
and can output more than 1 sentence, or even whole paragraph or topic if number of words that user looking for is more than % of text that have even some sense
in topic that we are looking for (yeah that also algorithms, but i already imagined it).


P.S.
I'd like to make an interface more interesting also.

"""""


def txt_read_and_write():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog to select one or multiple files
    file_paths = filedialog.askopenfilenames(title="Select Files",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    # Read the contents of the selected files
    file_contents = {}
    for path in file_paths:

        try:
            with open(path, "r", encoding="utf-8") as f:
                file_contents[path] = f.read()
        except Exception as e:
            print(f"Error reading file {path}: {e}")
    return file_contents, file_paths

def split_text(file_contents):
    return file_contents.split()

def char_count(file_contents):
    c_text = file_contents.lower()
    char_dict = dict(Counter(c_text))
    return char_dict

def sort_on(char_dict):
    sorted_char_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_char_dict


def display_output(path, file_contents,file_paths):

    global header_printed,files_ending

    total_files = len(file_paths)

    if not header_printed:
        print("============ BOOKBOT ============")
        header_printed = True

    print(f"Analyzing book found at {path}")

    # Word count
    print("----------- Word Count ----------")
    total_words = len(split_text(file_contents))
    print(f"Found {total_words} total words")

    # Character count
    print("--------- Character Count -------")
    char_dict = char_count(file_contents)
    sorted_characters = sort_on(char_dict)

    for char, count in sorted_characters:
        if char.strip():
            print(f"{char}: {count}")

    files_ending += 1

    if files_ending == total_files:
        print("============ ENDING ============")



