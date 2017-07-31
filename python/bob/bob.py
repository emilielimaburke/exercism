def hey(phrase):
	phrase = phrase.strip()
	if phrase == '':
		return('Fine. Be that way!')
	elif phrase.isupper() and phrase[-1] == "?":
		return('Whoa, chill out!')
	elif phrase[-1] == "?":
		return('Sure.')
	elif phrase.isupper():
		return('Whoa, chill out!')
	else:
		return('Whatever.')

##question mark followed by white space
