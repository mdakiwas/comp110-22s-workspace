"""Dictionary related utility functions."""

__author__ = "730474304"

from csv import DictReader
"""PART 0"""


def read_csv_rows(file: str) -> list[dict[str, str]]:
    """Reads CSV data into a list of rows."""
    result: list[dict[str, str]] = []

    # Opens handle to data file
    file_handle = open(file, "r", encoding="utf8")

    # Prepare to read data file as CSV, not strings
    csv_reader = DictReader(file_handle)

    # Read CSV rows
    for row in csv_reader:
        result.append(row)

    # Closes file 
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Returns all values in a column."""
    result: list[str] = []
    for row in table:
        value: str = row[column]
        result.append(value)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Changes row table into column table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


"""PART 1"""


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Returns the first N rows of data."""
    result: dict[str, list[str]] = {}
    for column in table:
        values: list[str] = []
        i = 0
        while i < n and i < len(table):
            values.append(table[column][i])
            i += 1
        result[column] = values
    return result


def select(table: dict[str, list[str]], col_name: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for column in col_name:
        result[column] = table[column]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column_key in table_2:
        if column_key in result:
            result[column_key] += table_2[column_key]
        else:
            result[column_key] = table_2[column_key]
    return result


"""PART 2"""


def count(values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for v in values:
        if v in result:
            result[v] += 1
        else:
            result[v] = 1
    return result