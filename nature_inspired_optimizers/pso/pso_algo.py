from matplotlib.pyplot import cla
import numpy as np
from typing import List, Callable, Tuple
from copy import deepcopy

from .particle import Particle

class PSOptimizer:

    def __init__(self, **kwargs):
        self.max_irterations: int = kwargs.get("max_irterations", 50)
        self.particle_num: int = kwargs.get("particle_num", 20)
        self.particles: List[Particle] = [Particle(**kwargs) for _ in range(self.particle_num)]

        self.global_best = deepcopy(max(self.particles))

    def optimize(self, max_iterations: int = None) -> Particle:
        max_iterations = max_iterations or self.max_irterations
        global_best = self.global_best

        for _ in range(max_iterations):

            for particle in self.particles:
                particle.step(global_best.position)

            global_best_ = max(self.particles)
            if global_best < global_best_:
                global_best = deepcopy(global_best_)

        self.global_best = global_best

        return global_best

    @property
    def best(self) -> Particle:
        return self.global_best