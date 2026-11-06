def reverse_words(text):
    """Reverse the order of words in a sentence."""
    return " ".join(text.split()[::-1])


def word_frequency(text):
    """Count how many times each word appears."""
    frequency = {}

    for word in text.lower().split():
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def remove_duplicate_characters(text):
    """Remove repeated characters while preserving order."""
    result = ""

    for char in text:
        if char not in result:
            result += char

    return result


def character_frequency(text):
    """Count the occurrence of each character."""
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency


def is_palindrome(text):
    """Check whether text reads the same forwards and backwards."""
    cleaned_text = "".join(
        char.lower() for char in text if char.isalnum()
    )

    return cleaned_text == cleaned_text[::-1]