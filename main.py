def main():
    book_path = "books/frankenstein.txt"
    text = get_text_from_book(book_path)
    num_words = get_num_words(text)
    print(remove_whitesepaces(text))

def count_letters_in_text(text):
    pass

def remove_whitesepaces(string):
    string = ''.join(string.split())
    return string

def get_num_words(text):
    words = text.split()
    return len(words)

    
def get_text_from_book(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()