from stats import *

if __name__ == "__main__":
    file_contents, file_paths = txt_read_and_write()  # Select and read files

    for path, content in file_contents.items():
        display_output(path, content, file_paths)