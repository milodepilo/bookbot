def main():
    book_path = "books/frankenstein.txt"
    text = get_text_from_book(book_path)
    num_words = get_num_words(text)
    letters_in_text = count_letters_in_text(text)
    list_of_dicts = dict_to_sorted_list(letters_in_text)
    
    print(f"--- begin report for {book_path} ---")
    print(f"{num_words} wwords found in the document")
    print()
    for item in list_of_dicts:
        print(f"the '{item['char']}' character was found {item['num']} times")
    print("--- end report ---")

def sort_on(d):
    return d["num"]


def dict_to_sorted_list(count_dict):
    sorted_list = []
    for ch in count_dict:
        sorted_list.append({"char": ch, "num": count_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def count_letters_in_text(text):
    text = text.lower()
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
