import sys
from stats import get_num_words, get_chars_dict, get_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    # Prüfen, ob der Pfad als Argument übergeben wurde
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Pfad aus den Kommandozeilenargumenten holen
    book_path = sys.argv[1]
    
    # Text laden
    text = get_book_text(book_path)
    
    # Daten verarbeiten
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = get_sorted_list(chars_dict)
    
    # Ausgabe im gewünschten Format
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
        
    print("============= END ===============")

if __name__ == "__main__":
    main()
