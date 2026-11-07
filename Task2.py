"""Tokenize sentences, filter stop words, and count word frequencies."""

STOP_WORDS = {"is", "the", "to", "a", "and", "in", "of"}

def tokenize(sentences):
    """Yield lowercase words from each sentence."""
    for sentence in sentences:
        for word in sentence.lower().split():
            yield word

def remove_stop_words(words):
    """Remove stop words from a sequence of words."""
    for word in words:
        if word not in STOP_WORDS:
            yield word

def count_frequency(words):
    """Count the frequency occurance os each word in a sentence"""
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    for word, count in frequency.items():
        yield (word, count)

sentences = [
    "Python is easy to learn"
]

tokens = tokenize(sentences)
filtered_words = remove_stop_words(tokens)
word_counts = count_frequency(filtered_words)

for word, count in word_counts:
    print(word, ":", count)