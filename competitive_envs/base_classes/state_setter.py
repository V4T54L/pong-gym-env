"""
Base state setter class.
"""
from abc import ABC, abstractmethod
from competitive_envs.base_classes.gamestate import GameState


class StateSetter(ABC):
    """Abstract class for State Setter.
    """

    @abstractmethod
    def reset(self, state: GameState):
        """
        Function to be called each time the environment is reset.

        :param state_wrapper: StateWrapper object to be modified with desired state values.

        NOTE: This function should change any desired values of the StateWrapper, which are all defaulted to 0.
        The values within StateWrapper are sent to the game each time the match is reset.
        """
        raise NotImplementedError
