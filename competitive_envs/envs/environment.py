"""
Base class for Match Environment.
"""

from abc import abstractmethod
from typing import Any, List
from competitive_envs.base_classes import GameState


class Environment:
    """
    Base class for Match Environment.
    """

    def __init__(self):
        """Initialize the env."""
        self.observation_space = None
        self.action_space = None
        self.agents = None
        self.bots = None
        self.team_size = None

    @abstractmethod
    def episode_reset(self, initial_state: GameState) -> None:
        """abstract method for reset."""
        raise NotImplementedError

    @abstractmethod
    def build_observations(self, state: GameState) -> List[Any]:
        """abstract method for building obs."""
        raise NotImplementedError

    @abstractmethod
    def get_rewards(self, state: GameState, done: bool) -> List[Any]:
        """abstract method for building rewards."""
        raise NotImplementedError

    @abstractmethod
    def is_done(self, state: GameState) -> bool:
        """abstract method for checking if terminal state is achieved."""
        raise NotImplementedError

    @abstractmethod
    def format_actions(self, actions: Any) -> List[Any]:
        """abstract method for formatting the actions."""
        raise NotImplementedError
