"""Dictionary exercise test."""

__author__ = "730474304"

from dictionary import invert, favorite_colors, count
import pytest


def test_invert_letters() -> None:
    """Inverting single letters."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_words() -> None:
    """Inverting words."""
    assert invert({'apple': 'cat', 'orange': 'dog'}) == {'cat': 'apple', 'dog': 'orange'}


with pytest.raises(KeyError):
    """Testing whether the key error would show when there would be more than one of the same key."""
    dictionary = {'MJ': 'red', 'John': 'red'}
    invert(dictionary)


def test_favorite_color_short() -> None:
    """Asserting most favorite color from 3 keys."""
    name_color = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_colors(name_color) == "blue"


def test_favorite_color_long() -> None:
    name_color = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Marley": "purple", "MJ": "red", "John": "blue"}
    assert favorite_colors(name_color) == "blue"


def test_favorite_color_tie() -> None:
    """Testing whether the first mentioned favorite color would return in the case of a tie."""
    name_color = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Marley": "purple", "MJ": "red", "John": "red"}
    assert favorite_colors(name_color) == "blue"


def test_count_short() -> None:
    """Counts the amount of time an animal is in the list."""
    keys = ["raccoon", "panda", "polar bear", "panda"]
    assert count(keys) == {"raccoon": 1, "panda": 2, "polar bear": 1}


def test_count_single() -> None:
    """Testing whether returned values would be all 1."""
    keys = ["raccoon", "panda", "polar bear", "red panda"]
    assert count(keys) == {"raccoon": 1, "panda": 1, "polar bear": 1, "red panda": 1}


def test_count_more() -> None:
    """Testing whether returned values can be a large number."""
    keys = ["raccoon", "panda", "polar bear", "panda", "raccoon", "panda", "raccoon", "polar bear", "panda"]
    assert count(keys) == {"raccoon": 3, "panda": 4, "polar bear": 2}
