"""Chardle it's chardle, chardle!"""

__author__ = "730474304"

"""User input for 5 letter word."""
five_char_word: str = input("Enter a 5-character word: ")
if len(five_char_word) != 5:
    """If invalid input, quiting program."""
    print("Error: Word must contain 5 characters")
    exit()

"""User input for 1 character."""
single_char: str = input("Enter a single character: ")
if len(single_char) != 1:
    """If invalid input, quiting program."""
    print("Error: Character must be a single character")
    exit()

print("Searching for " + single_char + " in " + five_char_word)

char_match: int = 0
"""Check five indices of word."""
if five_char_word[0] == single_char:
    print(single_char + " found at index 0")
    char_match = char_match + 1
if five_char_word[1] == single_char:
    print(single_char + " found at index 1")
    char_match = char_match + 1
if five_char_word[2] == single_char:
    print(single_char + " found at index 2")
    char_match = char_match + 1
if five_char_word[3] == single_char:
    print(single_char + " found at index 3")
    char_match = char_match + 1
if five_char_word[4] == single_char:
    print(single_char + " found at index 4")
    char_match = char_match + 1

if char_match >= 2:
    print(str(char_match) + " instances of " + single_char + " found in " + five_char_word)
else:
    print(str(char_match) + " instance of " + single_char + " found in " + five_char_word)

if char_match == 0:
    print("No instances of " + single_char + " found in " + five_char_word)