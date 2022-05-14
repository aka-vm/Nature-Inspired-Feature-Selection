from turtle import pos
import numpy as np

from ..utils.point import Point

class Wolf(Point):

    def __move_towards(self, targate_position: np.ndarray, a_parameter: float) -> np.ndarray:
        a_vector = 2 * a_parameter * np.random.random(self.dimensions) - a_parameter
        c_vector = 2 * np.random.random(self.dimensions)

        d_vector = np.abs(c_vector * targate_position - self.position)

        return targate_position - a_vector * d_vector

    def move(self, a_parameter: np.ndarray,
             alpha_position: np.ndarray,
             beta_position:  np.ndarray,
             delta_position: np.ndarray) -> None:

        x_1 = self.__move_towards(alpha_position, a_parameter)
        x_2 = self.__move_towards(beta_position, a_parameter)
        x_3 = self.__move_towards(delta_position, a_parameter)

        self.position = (x_1 + x_2 + x_3)/3