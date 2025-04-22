from stats import chars_dict_to_sorted_list, get_num_chars, get_num_words
import sys

def print_report(path, word_count, chars_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Get sorted list of character dictionaries
    sorted_chars = chars_dict_to_sorted_list(chars_dict)
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

def main(book_path):
    with open(book_path, "r") as f:
        file_contents = f.read()
        word_count = get_num_words(file_contents)
        chars_dict = get_num_chars(file_contents)
        print_report(book_path, word_count, chars_dict)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])