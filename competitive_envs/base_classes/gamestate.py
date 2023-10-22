"""Abstract GameState
"""

from typing import List
from competitive_envs.base_classes.player_data import PlayerData


class GameState(object):
    """Abstract gamestate class"""

    def __init__(self) -> None:
        """Initialize GameState"""
        self.players: List[PlayerData] = []
