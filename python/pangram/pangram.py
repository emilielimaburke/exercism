import re

def is_pangram(pangram):
	"""Determine if a sentence is a pangram."""
	pangram = re.sub(r'[\W]', '', pangram)
	pangram = re.sub(r'[_0-9]', '', pangram)
	output = set(pangram.lower())
	return len(output) == 26

print(is_pangram('the quick brown fox jumped over the lazy FOX'))

#pangram = re.sub(r'[a-zA-Z]', '', pangram)