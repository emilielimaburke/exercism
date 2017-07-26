import re

def word_count(phrase):
    """Given a phrase, count the occurrences of each word in that phrase."""
    phrase = phrase.lower()
    phrase = re.sub(r'[^a-z0-9]+', ' ', phrase)
    words = phrase.split()
    wordfreq = [words.count(p) for p in words]
    return dict(zip(words, wordfreq))
