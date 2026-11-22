# Import third party packages.
import numpy as np

# Import local packages.
from src.agents.base import Agent


class TabularAgent(Agent):
    def __init__(
        self, n_cues: int, learning_rate: float, initial_value: float = 0.0
    ) -> None:
        """
        Constructor for the TabularAgent class.

        Args:
            n_cues (int):
                Number of distinct cues. Cues are integer indices.

            learning_rate (float):
                Step size (alpha) used in every update.

            initial_value (float, optional):
                Starting value for all cues. Defaults to 0.0.
        """
        self.learning_rate = learning_rate
        self.values = np.full(n_cues, initial_value, dtype=float)

    def predict(self, cue: int) -> float:
        return float(self.values[cue])

    def update(self, cue: int, reward: float) -> float:
        td_error = reward - self.predict(cue)
        self.values[cue] += self.learning_rate * td_error
        return td_error
