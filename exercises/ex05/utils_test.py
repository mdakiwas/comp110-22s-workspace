"""Utility test."""

__author__ = "730474304"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    "only_evens Function test odds and evens."
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_odds() -> None:
    "only_evens Function test only odds."
    assert only_evens([1, 5, 3]) == []


def test_only_evens_evens() -> None:
    "only_evens Function test only evens."
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_sub() -> None:
    "sub Function test four int range."
    num_list = [10, 20, 30, 40]
    assert sub(num_list, 1, 3) == [20, 30]


def test_sub_1() -> None:
    "sub Function test five int range."
    num_list = [50, 60, 70, 80, 90]
    assert sub(num_list, 2, 4) == [70, 80]


def test_sub_2() -> None:
    "sub Function test seven int range."
    num_list = [11, 22, 33, 44, 55, 66, 77]
    assert sub(num_list, 2, 6) == [33, 44, 55, 66]


def test_concat() -> None:
    "concat Function test single digit int."
    list_one = [1, 2, 3]
    list_two = [4, 5, 6]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_1() -> None:
    "concat Function test double digit int."
    list_one = [10, 20, 30, 40]
    list_two = [50, 60, 70]
    assert concat(list_one, list_two) == [10, 20, 30, 40, 50, 60, 70]


def test_concat_2() -> None:
    "concat Function test complex int."
    list_one = [7, 17, 237, 397]
    list_two = [427, 507, 67, 767]
    assert concat(list_one, list_two) == [7, 17, 237, 397, 427, 507, 67, 767]