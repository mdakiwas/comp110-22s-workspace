"""'list' Utility Functions."""

__author__ = "730474304"


def only_evens(num_list: list[int]) -> list[int]:
    evens: list[int] = []
    for num in num_list:
        if num % 2 == 0:
            evens.append(num)
    return evens


def sub(num_list: list[int], start_i: int, end_i: int) -> list[int]:
    subset: list[int] = []
    start: int = 0
    end: int = len(num_list)
    if start_i < 0:
        start = 0
    if end_i > len(num_list):
        end = len(num_list)
    if len(num_list) == 0 or start_i > len(num_list) or end_i <= 0:
        return []
    while start < end:
        if start >= start_i and start < end_i:
            subset.append(num_list[start])
        start += 1
    return subset


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    new_list: list[int] = []
    new_list = list_one + list_two
    return new_list