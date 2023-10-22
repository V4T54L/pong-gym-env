"""Implement Match class"""
from typing import Any, List
import numpy as np
from competitive_envs.envs.environment import Environment
from competitive_envs.base_classes import (
    GameState,
    RewardFunction,
    TerminalCondition,
    ObsBuilder,
    ActionParser,
    StateSetter,
)


class Match(Environment):
    """Match class for Gym env."""

    def __init__(
        self,
        reward_function: RewardFunction,
        terminal_conditions: TerminalCondition,
        obs_builder: ObsBuilder,
        action_parser: ActionParser,
        state_setter: StateSetter,
        sample_game_action: Any,
        team_size: int = 1,
        spawn_opponents: bool = True,
    ) -> None:
        super().__init__()
        self._reward_function = reward_function
        self._terminal_conditions = terminal_conditions
        self._obs_builder = obs_builder
        self._action_parser = action_parser
        self._state_setter = state_setter
        self.team_size = team_size
        self.spawn_opponents = spawn_opponents

        self.n_agents = team_size if not spawn_opponents else team_size * 2
        self.observation_space = obs_builder.get_obs_space()

        assert (
            self.observation_space is not None
        ), "obs_builder.get_obs_space() returned None"

        self.action_space = action_parser.get_action_space()
        assert (
            self.action_space is not None
        ), "action_parser.get_action_space() returned None"

        self._prev_actions = np.asarray(
            [sample_game_action for _ in range(self.n_agents)]
        )

    def episode_reset(self, initial_state: GameState) -> None:
        """Reset the episode

        Args:
            initial_state (Initial state of the game): _description_
        """
        self._prev_actions.fill(0)
        for condition in self._terminal_conditions:
            condition.reset(initial_state)
        self._reward_fn.reset(initial_state)
        self._obs_builder.reset(initial_state)

    def build_observations(self, state: GameState) -> List[Any]:
        """Build Observation for Game

        Args:
            state (GameState): _description_

        Returns:
            Union[Any, List]: _description_
        """
        observations = []

        self._obs_builder.pre_step(state)

        for i, player in enumerate(state.players):
            obs = self._obs_builder.build_obs(player, state, self._prev_actions[i])
            observations.append(obs)

        return observations

    def get_rewards(self, state: GameState, done: bool) -> List[Any]:
        """Get Rewards

        Args:
            state (GameState): Current State
            done (bool): If terminal condition reached

        Returns:
            _type_: List[Rewards]
        """
        rewards = []

        self._reward_fn.pre_step(state)
        for i, player in enumerate(state.players):
            if done:
                reward = self._reward_fn.get_final_reward(
                    player, state, self._prev_actions[i]
                )
            else:
                reward = self._reward_fn.get_reward(
                    player, state, self._prev_actions[i]
                )

            rewards.append(reward)

        if len(rewards) == 1:
            return rewards[0]

        return rewards

    def is_done(self, state: GameState) -> bool:
        for condition in self._terminal_conditions:
            if condition.is_terminal(state):
                return True
        return False

    def parse_actions(self, actions: Any, state: GameState) -> np.ndarray:
        # Prevent people from accidentally modifying numpy arrays inside the ActionParser
        if isinstance(actions, np.ndarray):
            actions = np.copy(actions)
        return self._action_parser.parse_actions(actions, state)

    def format_actions(self, actions: np.ndarray) -> List[Any]:
        self._prev_actions[: len(actions)] = actions[:]
        acts = []
        for i in range(len(actions)):
            acts.append(float(self._spectator_ids[i]))
            for act in actions[i]:
                acts.append(float(act))

        return acts

    def get_reset_state(self) -> List:
        new_state = self._state_setter.build_wrapper(
            self.team_size, self.spawn_opponents
        )
        self._state_setter.reset(new_state)
        return new_state.format_state()
