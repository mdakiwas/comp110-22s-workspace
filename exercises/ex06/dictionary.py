"""Dictionaries would be the end of me."""

__author__ = "730474304"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the key and value of the inputted dictionary."""
    inverted_dict: dict[str, str] = {}
    for key, value in dictionary.items():
        if value not in inverted_dict:
            inverted_dict[value] = key
        else:
            raise KeyError(value)
    return inverted_dict


def favorite_colors(name_color: dict[str, str]) -> str:
    """Returns the most favorite color/value."""
    colors = list(name_color.values())
    most_fav_color = max(colors, key=colors.count)
    return most_fav_color


def count(keys: list[str]) -> dict[str, int]:
    """Counts the amount of times the key is in the inputted list and returns as the value."""
    dictionary: dict[str, int] = {}
    for item in keys:
        if item in dictionary.keys():
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary