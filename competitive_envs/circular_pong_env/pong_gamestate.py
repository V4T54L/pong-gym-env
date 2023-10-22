"""Pong Gamestate
"""

from typing import List
from competitive_envs.base_classes import GameState
from competitive_envs.circular_pong_env.pong_object_data import (
    PongBallData,
    PongPlayerData,
)


class PongGameState(GameState):
    def __init__(
        self,
        stadium_width: int,
        stadium_length: int,
        player_radius: int,
        ball_radius: int,
        movement_speed: float,
    ) -> None:
        player_y = stadium_width // 2
        self.players: List[PongPlayerData] = [
            PongPlayerData(
                player_radius, stadium_width=stadium_width, x=player_radius, y=player_y
            ),
            PongPlayerData(
                player_radius,
                stadium_width=stadium_width,
                x=stadium_length - player_radius,
                y=player_y,
            ),
        ]
        self.ball = PongBallData(
            ball_radius,
            stadium_length // 2,
            stadium_width // 2,
            5,
            5,
            stadium_length,
            stadium_width,
            player_radius,
        )
        self.score = [0, 0]
        self.movement_speed = movement_speed
