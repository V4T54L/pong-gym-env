"""Implement Match class"""
from typing import Any, Union, List
import numpy as np
from competitive_envs.base_classes import (
    PlayerData,
    GameState,
    ObsBuilder,
    ActionParser,
    RewardFunction,
    StateSetter,
    TerminalCondition,
)
from competitive_envs.envs import Match


class PongMatch(Match):
    """Match class for Gym env."""

    def __init__(
        self,
        reward_function: RewardFunction,
        terminal_conditions: TerminalCondition,
        obs_builder: ObsBuilder,
        action_parser: ActionParser,
        state_setter: StateSetter,
        sample_game_action: Any,
    ) -> None:
        super().__init__(
            reward_function,
            terminal_conditions,
            obs_builder,
            action_parser,
            state_setter,
            sample_game_action,
            team_size=1,
            spawn_opponents=True,
        )

    def build_observations(self, state: GameState) -> np.array:
        return super().build_observations(state)
