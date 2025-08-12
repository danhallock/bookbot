from stats import count_words
from stats import count_letters
from stats import sort_letter_count

def get_book_text(path):
	with open(path) as b:
		text = b.read()
		return text

def main():
	path = 'books/frankenstein.txt'
	f = get_book_text(path)
	w = count_words(f)
	c = count_letters(f)
	s = sort_letter_count(c)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {w} total words.")
	print("--------- Character Count -------")
	for letter in s:
		if letter['letter'].isalpha():
			print(f"{letter['letter']}: {letter['count']}")
	print("============= END ===============")

main()
