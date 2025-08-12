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

def sort_on_letter_count(letter_count):
	return letter_count["count"]

def sort_letter_count(letter_count):
	sortable_list = []
	for letter, count in letter_count.items():
		sortable_list.append({'letter': letter, 'count': count})
	sortable_list.sort(reverse=True, key=sort_on_letter_count)
	return sortable_list
