from math import gamma
import numpy as np
from typing import List, Callable
from copy import deepcopy

from .wolf import Wolf

class GWOptimizer:

    def __init__(self, **kwargs):
        self.max_irterations: int = kwargs.get("max_irterations", 20)
        self.wolf_num: int = kwargs.get("wolf_num", 20)
        self.__wolves: List[Wolf] = [Wolf(**kwargs) for _ in range(self.wolf_num)]

    def optimize(self, max_irterations: int = None) -> Wolf:
        max_irterations = max_irterations or self.max_irterations
        alpha, beta, delta = self.get_alpha_beta_delta
        best = deepcopy(alpha)

        for i in range(max_irterations):
            a_parameter = 2 * ((1 - i) / max_irterations)

            for wolf in self.__wolves:
                wolf.move(a_parameter, alpha.position, beta.position, delta.position)

            alpha_, beta_, delta_ = self.get_alpha_beta_delta

            if alpha_ > alpha:
                alpha = alpha_

            if beta_ > beta:
                beta = beta_

            if delta_ > delta:
                delta = delta_

            if best < alpha:
                best = deepcopy(alpha)

        return best

    @property
    def get_alpha_beta_delta(self) -> tuple[Wolf, Wolf, Wolf]:
        best_three_i = np.argsort(self.__wolves)[-3:]
        return [deepcopy(self.__wolves[i]) for i in best_three_i]