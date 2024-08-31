def main():
    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)
    word_count = count_words(book_text)
    print(f"word count: {word_count}")
    char_dict = count_characters(book_text)
    print(f"char count: {char_dict}")
    
    
def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    # count the number of characters repeated in the text and returns a dictionary of char -> count
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


if __name__ == '__main__':
    main()
    
    