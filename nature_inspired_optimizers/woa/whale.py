import numpy as np

from ..utils.point import Point

class Whale(Point):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__b: float = kwargs.get("b", 1.0)

    def __step_towards(self, targate_position: np.ndarray, a_parameter: float) -> np.ndarray:
        a_vector = 2 * a_parameter \
                    * np.random.random(self.dimensions) \
                    - a_parameter

        c_vector = 2 * np.random.random(self.dimensions)

        d_vector = np.abs(
                        c_vector
                        * targate_position
                        - self.position)

        return targate_position - a_vector * d_vector

    def encircle_prey(self, prey_position: np.ndarray, a_parameter: float) -> None:
        self.position = self.__step_towards(
                                    prey_position,
                                    a_parameter)

    def search_prey(self, a_parameter: float) -> None:
        random_targate = self.rand_fnx(
                                self.mid_point,
                                self.scale_length,
                                self.dimensions)

        self.position = self.__step_towards(
                                random_targate,
                                a_parameter)

    def attack_prey(self, prey_position: np.ndarray) -> None:
        d_vector = np.abs(
                        prey_position
                        - self.position)
        l = np.random.uniform(-1., 1.)

        self.position = d_vector * \
                        np.exp(self.__b * l) * \
                        np.cos(2 * np.pi * l) + \
                        prey_position
