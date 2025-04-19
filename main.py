import sys
from stats import analyze_book, num_words, letter_counter

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

book_path = sys.argv[1]

print("============ BOOKBOT ============")
print(f"Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
word_count = num_words(book_path) #call function and get the result
print(f"Found {word_count} total words")
print("--------- Character Count -------")
letter_counts = letter_counter(book_path) #call function and get the result
for letter, count in letter_counts:
	print(f"{letter}: {count}")
print("============= END ===============")

