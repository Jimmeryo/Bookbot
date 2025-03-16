from stats import *
import sys

if __name__ == "__main__":
    files = txt_read_and_write()  # Select and read files

    if files:
        for path, content in files.items():
            display_output(path, content)  # Pass the file path and content to display_output
    else:
        print("No files selected.")
