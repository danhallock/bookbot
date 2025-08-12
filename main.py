from stats import count_words
from stats import count_letters

def get_book_text(path):
	with open(path) as b:
		text = b.read()
		return text

def main():
	f = get_book_text('books/frankenstein.txt')
	c = count_letters(f)
	print(f"{c}")

main()
