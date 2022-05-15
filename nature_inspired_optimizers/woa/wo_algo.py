import numpy as np
from typing import List, Callable, Tuple
from copy import deepcopy

from .whale import Whale

class WhaleOptimizer:

    def __init__(self, **kwargs):
        self.max_irterations: int = kwargs.get("max_irterations", 50)
        self.whale_num: int = kwargs.get("whale_num", 20)
        self.whales: List[Whale] = [Whale(**kwargs) for _ in range(self.whale_num)]

        self.best = deepcopy(max(self.whales))

    def optimize(self, max_iterations: int = None) -> Whale:
        max_iterations = max_iterations or self.max_irterations
        best = self.best

        for i in range(max_iterations):
            a_parameter = 2 * ((1 - i) / max_iterations)

            for whale in self.whales:
                prob: float = np.random.uniform()

                if prob < 0.5:
                    if a_parameter < 1:
                        whale.encircle_prey(best.position, a_parameter)
                    else:
                        whale.search_prey(a_parameter)
                else:
                    whale.attack_prey(best.position)

                whale.update_fitness_value()

            best_ = max(self.whales)
            if best < best_:
                best = deepcopy(best_)

        self.best = best

        return best