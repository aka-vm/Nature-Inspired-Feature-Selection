import numpy as np

from utils.point import Point

class FireFly(Point):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__alfa: float = kwargs.get("alfa", 1e-1)
        self.__beta: float = kwargs.get("beta", 1)
        self.__gamma: float = kwargs.get("gamma", 1 / (self.scale_length * self.dimensions**0.5))

    def move_towards(self, other: "FireFly") -> None:
        dist_v = other.position - self.position

        self.position = self.position + \
                        self.__beta * np.exp(-self.__gamma * np.linalg.norm(dist_v) ** 2) * dist_v + \
                        self.__alfa * self.random_targate()

    def random_targate(self, area:float=0.1) -> np.ndarray:
        scale_length = np.abs(self.upper_bound - self.lower_bound) / 2
        return self.rand_fnx(0, scale_length, self.dimensions) * area