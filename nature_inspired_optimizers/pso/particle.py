from copy import deepcopy
import numpy as np

from ..utils.point import Point

class Particle(Point):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__w    = kwargs.get("w", 0.1)
        self.__c_1  = kwargs.get("c_1", 0.2)    # Personal
        self.__c_2  = kwargs.get("c_2", 0.2)    # Social/Global

        v_max           = kwargs.get("v_max", self.scale_length/2)
        self.__v_max    = v_max
        self.__v        = np.random.uniform(-v_max/2, v_max/2, self.dimensions)

        self.best_position      = self.position
        self.best_fitness_value = self.fitness_value

    def step(self, global_best_position: np.ndarray) -> None:
        r1 = np.random.uniform()
        r2 = np.random.uniform()

        velocity =  self.__w * self.velocity \
                    + self.__c_1 * r1 * (self.best_position - self.position) \
                    + self.__c_2 * r2 * (global_best_position - self.position)
        self.velocity = velocity

        position = self.position + velocity
        self.position = position
        self.update_fitness_value()

        if self.fitness_value > self.best_fitness_value:
            self.best_position = deepcopy(position)
            self.best_fitness_value = self.fitness_value

    @property
    def velocity(self):
        return self.__v

    @velocity.setter
    def velocity(self, new_velocity):
        v_max = self.__v_max
        self.__v = np.clip(new_velocity, -v_max, v_max)