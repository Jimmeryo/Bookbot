
def txt_read_and_write ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def main():
    s_text = txt_read_and_write()
    print(len(txt_read_and_write().split()),"words found in the document")

if __name__ == "__main__":
    main()