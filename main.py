def main():
    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)
    word_count = count_words(book_text)
    print(f"word count: {word_count}")
    
def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


def count_words(text):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    main()
    
    