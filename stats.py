#define book path
def analyze_book(book_path):
	with open(book_path) as f:
		file_contents = f.read()
		return file_contents
#count words
def num_words(book_path):
	words = analyze_book(book_path).split()
	return len(words)
# count letters
def letter_counter(book_path):
	letter_count = {}
	f_lower = analyze_book(book_path).lower()
	words = f_lower.split()
	for word in words:
		for let in word:
			if let.isalpha():
				letter_count[let] = letter_count.get(let, 0) + 1
	sorted_letters = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
	return(sorted_letters)
