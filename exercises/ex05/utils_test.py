"""'Utility test."""

__author__ = "730474304"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_1() -> None:
    assert only_evens([1, 5, 3]) == []


def test_only_evens_2() -> None:
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_sub() -> None:
    num_list = [10, 20, 30, 40]
    assert sub(num_list, 1, 3) == [20, 30]


def test_sub_1() -> None:
    num_list = [50, 60, 70, 80, 90]
    assert sub(num_list, 2, 4) == [70, 80]


def test_sub_2() -> None:
    num_list = [11, 22, 33, 44, 55, 66, 77]
    assert sub(num_list, 2, 6) == [33, 44, 55, 66]


def test_concat() -> None:
    list_one = [1, 2, 3]
    list_two = [4, 5, 6]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_1() -> None:
    list_one = [10, 20, 30, 40]
    list_two = [50, 60, 70]
    assert concat(list_one, list_two) == [10, 20, 30, 40, 50, 60, 70]


def test_concat_2() -> None:
    list_one = [7, 17, 27, 37]
    list_two = [47, 57, 67, 77]
    assert concat(list_one, list_two) == [7, 17, 27, 37, 47, 57, 67, 77]