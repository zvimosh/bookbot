def main():
    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)
    word_count = count_words(book_text)
    chars_dict = get_chars_dict(book_text)
    print(f"--- begin report for {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")
    
    
def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    # count the number of characters repeated in the text and returns a dictionary of char -> count
    chars = {}
    for c in text:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def chars_dict_to_sorted_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num": dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(d):
    return d["num"]
    

if __name__ == '__main__':
    main()
    
    