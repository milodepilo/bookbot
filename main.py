def main():
    book_path = "books/frankenstein.txt"
    text = get_text_from_book(book_path)
    num_words = get_num_words(text)
    print(count_letters_in_text(text))

def count_letters_in_text(text):
    text= text.lower()
    c = {}
    for letter in text:        
        if letter.isalpha():
            if letter in c:
                c[letter] += 1
            else:
                c[letter] = 1
    return c



def get_num_words(text):
    words = text.split()
    return len(words)

    
def get_text_from_book(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()