import numpy as np
from typing import Callable

from .functions import uniform_random_vector
from .errors import fitness_function_not_implemented

class Point:

    def __init__(self, **kwargs) -> None:
        self.dimensions: int    = kwargs["dimensions"]
        self.fitness_value: float   = 0.0
        self.__position: np.ndarray   = np.zeros(self.dimensions)

        self.lower_bound: float = kwargs.get("lower_boud", 0.0)
        self.upper_bound: float = kwargs.get("upper_boud", 1.0)
        self.scale_length: float = np.abs(self.upper_bound - self.lower_bound) / 2
        self.mid_point: float = (self.upper_bound + self.lower_bound) / 2

        self.rand_fnx: Callable = kwargs.get("ranf_fxn", uniform_random_vector)
        self.fitness_function: Callable   = kwargs.get("fitness_function", fitness_function_not_implemented)

        self.__initalize()
        self.update_fitness_value()

    def __initalize(self) -> None:
        mean_ = (self.upper_bound + self.lower_bound) / 2
        self.position = self.rand_fnx(mean_, self.scale_length, self.dimensions)

    @property
    def position(self) -> np.ndarray:
        return self.__position

    @property
    def distance(self) -> float:
        return np.linalg.norm(self.position)

    @position.setter
    def position(self, new_position: np.ndarray) -> None:
        self.__position = np.clip(new_position, a_min=self.lower_bound, a_max=self.upper_bound)

    def update_fitness_value(self) -> None:
        self.fitness_value = self.fitness_function(self.position)

    def __str__(self) -> str:
        return f"{self.position.shape} - [{self.fitness_value}]"

    def __repr__(self) -> str:
        return f"{self.position.shape} - [{self.fitness_value}]"

    def __eq__(self, other: "Point") -> bool:
        return np.array_equal(self.fitness_value, other.fitness_value)

    def __ne__(self, other: "Point") -> bool:
        return not np.array_equal(self.fitness_value, other.fitness_value)

    def __lt__(self, other: "Point") -> bool:
        return self.fitness_value < other.fitness_value

    def __le__(self, other: "Point") -> bool:
        return self.fitness_value <= other.fitness_value

    def __gt__(self, other: "Point") -> bool:
        return self.fitness_value > other.fitness_value

    def __ge__(self, other: "Point") -> bool:
        return self.fitness_value >= other.fitness_value
