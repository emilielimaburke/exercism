import re

def is_isogram(isogram):
	"""Determine if a word or phrase is an isogram."""
	isogram = re.sub(r'\W+', '', isogram)
	output = set(isogram.lower())
	lower = isogram.lower()
	return len(lower) == len(output)
