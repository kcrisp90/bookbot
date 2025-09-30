import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        #return #this was blocking the traceback that the cli wanted
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    char_counts = get_char_counts(text)
    #print(char_counts)

    sorted_chars = sort_char_counts(char_counts)
    #print(sorted_chars)

    print("--------- Character Count -------")

    for item in sorted_chars[:]:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")

    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()