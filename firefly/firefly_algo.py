from math import gamma
import numpy as np
from typing import List, Callable
from copy import deepcopy

from .firefly import FireFly


class FireflyOptimizer:

    def __init__(self, **kwargs) -> None:
        self.max_irterations: int = kwargs.get("max_irterations", 20)
        self.fireflies_num: int = kwargs.get("fireflies_num", 100)
        self.__fireflies = [FireFly(**kwargs) for _ in range(self.fireflies_num)]

    def optimize(self) -> List[FireFly]:
        best = deepcopy(max(self.__fireflies))
        for _ in range(self.max_irterations):
            for firefly in self.__fireflies:
                for targate_firefly in self.__fireflies:
                    if firefly < targate_firefly:
                        firefly.move_towards(targate_firefly)

            temp_best = max(self.__fireflies)
            if best < temp_best:
                best = deepcopy(temp_best)

            temp_best.position += temp_best.random_targate()

        return self.__fireflies