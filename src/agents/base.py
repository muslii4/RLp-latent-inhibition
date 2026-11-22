# Import standard library packages.
from abc import ABC, abstractmethod


class Agent(ABC):
    @abstractmethod
    def predict(self, cue: int) -> float:
        """
        Predict the expected reward for a given cue index.

        Args:
            cue (int): The input cue.

        Returns:
            float: The predicted reward.
        """
        pass

    @abstractmethod
    def update(self, cue: int, reward: float) -> float:
        """
        Learn from one trial and return the temporal
        difference (TD) error computed before the update.

        Args:
            cue (int): The input cue.
            reward (float): The observed reward.

        Returns:
            float: The TD error.
        """
