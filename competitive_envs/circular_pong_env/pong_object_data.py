"""Pong PlayerData
"""

from sympy import rad
from competitive_envs.base_classes import PlayerData


class PongPlayerData(PlayerData):
    """Pong Player Data"""

    def __init__(self, radius: int, stadium_width: int, x: float, y: float = 0) -> None:
        self.x: float = x
        self.y: float = y
        self.radius = radius
        self.border_y = stadium_width - radius

    def step(self, del_y: float) -> None:
        """Player Step

        Args:
            del_y (float): delta change in y position
        """
        self.y += del_y

        if self.y < 0:
            self.y *= -1
        elif self.y > self.border_y:
            self.y -= self.border_y


class PongBallData(object):
    """Ball Data"""

    def __init__(
        self,
        radius: int,
        pos_x: int,
        pos_y: int,
        vel_x: float,
        vel_y: float,
        stadium_len: int,
        stadium_width: int,
        player_radius: int,
    ) -> None:
        self.radius = radius
        self.pos_x: float = pos_x
        self.pos_y: float = pos_y
        self.vel_x: float = vel_x
        self.vel_y: float = vel_y
        self.border_x = stadium_len - radius
        self.border_y = stadium_width - radius
        self.min_dist_sq = (player_radius + radius) ** 2

    def __check_collision(
        self,
        player: PongPlayerData,
    ):
        return (
            (self.pos_x - player.x) ** 2 + (self.pos_y - player.y) ** 2
        ) <= self.min_dist_sq

    def handle_collision(self, player: PongPlayerData) -> None:
        """updates params if collides with the player

        Args:
            player (PongPlayerData): Player to check collision against
        """
        if self.__check_collision(player):
            raise NotImplementedError

    def step(self) -> None:
        """Ball Step"""
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

        if self.pos_x < 0:
            self.pos_x *= -1
        elif self.pos_x > self.border_x:
            self.pos_x -= self.border_x

        if self.pos_y < 0:
            self.pos_y *= -1
        elif self.pos_y > self.border_y:
            self.pos_y -= self.border_y
