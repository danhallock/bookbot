def count_words(text):
	words = text.split()
	return len(words)

def count_letters(text):
	per_letter_count = {}
	for char in text:
		c = char.lower()
		if c in per_letter_count:
			per_letter_count[c] += 1
		else:
			per_letter_count[c] = 1
	return per_letter_count
