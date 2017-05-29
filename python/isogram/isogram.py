import re

def is_isogram(isogram):
	isogram = re.sub(r'\W+', '', isogram)
	output = set(isogram.lower())
	lower = isogram.lower()
	if len(lower) <= len(output):
		return True
	else:
		return False