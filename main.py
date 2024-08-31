def main():
    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)
    word_count = count_words(book_text)
    print(f"word count: {word_count}")
    char_dict = get_chars_dict(book_text)
    print(f"char count: {char_dict}")
    
    
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


if __name__ == '__main__':
    main()
    
    