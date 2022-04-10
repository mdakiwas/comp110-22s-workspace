"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730474304"


class Simpy:
    values: list[float]

    def __init__(self, initialize: list[float]) -> None:
        """Initialize the values of the object to the argument."""
        self.values = initialize

    def __str__(self) -> str:
        """Called when object is converted to a str representation."""
        return f"Simpy({self.values})"

    def fill(self, filling: float, repeat: int) -> None:
        """Fill the object's vaues with a specific number of repeating values."""
        self.values = []
        i = 0
        while i < repeat:
            self.values.append(filling)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values with range of values."""
        assert step != 0.0
        self.values = []
        if start < stop:
            while start < stop:
                self.values.append(start)
                start += step
        elif start > stop:
            while start > stop:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Compute and return the sum of all items in the values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Use the addition operator in conjunction with Simpy objects and floats."""
        if isinstance(rhs, float):
            result: list[float] = []
            for i in self.values:
                result.append(i + rhs)
            return Simpy(result)
        else:
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
            return Simpy(result)
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Use the power operator in conjunction with Simpy objects and floats."""
        if isinstance(rhs, float):
            result: list[float] = []
            for i in self.values:
                result.append(i ** rhs)
            return Simpy(result)
        else:
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
            return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a list of booleans by comparing whether the values of Simpy objects are equal."""
        if isinstance(rhs, float):
            result: list[bool] = []
            for i in self.values:
                if i == rhs:
                    result.append(True)
                else:
                    result.append(False)
            return result
        else:
            result: list[bool] = []
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
            return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a list of booleans by comparing whether the values of a Simpy object is greater than the other Simpy's values."""
        if isinstance(rhs, float):
            result: list[bool] = []
            for i in self.values:
                if i > rhs:
                    result.append(True)
                else:
                    result.append(False)
            return result
        else:
            result: list[bool] = []
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
            return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Filters through a Simpy object to select individual items."""
        if isinstance(rhs, int):
            return self.values[rhs]      
        else:
            result: list[float] = []
            for i in range(len(self.values)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result)
