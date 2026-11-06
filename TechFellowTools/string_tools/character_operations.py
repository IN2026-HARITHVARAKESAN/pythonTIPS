def count_lowercase_letters(s):
    """Count the number of lowercase letters in a string."""
    sum = 0
    for char in s:
        if char.islower():
            sum+=1
    return sum

def count_uppercase_letters(s):
    """Count the number of uppercase letters in a string."""
    sum = 0
    for char in s:
        if char.isupper():
         sum+=1
    return sum

def count_digits(s):
    """Count the number of digits in a string."""
    sum = 0
    for char in s:
        if char.isdigit():
            sum+=1
    return sum

def get_middle_character(s):
    """Return the middle character of a string."""
    length = len(s)
    if length == 0:
        return ""
    mid_index = length // 2
    if length % 2 == 0:
        new=s[mid_index-1]+s[mid_index]
        return new
    else:
        return s[mid_index]

def get_unique_characters(s):
    """Return a string containing only unique characters."""
    unique_chars = ""
    for char in s:
        if s.count(char) == 1:
            unique_chars += char
    return unique_chars