# env/environment.py

import gymnasium as gym
from gymnasium import spaces
import numpy as np
from typing import List, Tuple, Optional

from .models import Email
from .grader import Grader


class InboxEnv(gym.Env):
    def __init__(self, emails: Optional[List[Email]] = None):
        super().__init__()

        self.emails = emails or []
        self.current_index = 0
        self.current_email: Optional[Email] = None

        self.grader = Grader()

        self.action_space = spaces.Discrete(4)

        self.observation_space = spaces.Box(
            low=0,
            high=10,
            shape=(2,),
            dtype=np.float32
        )

    def reset(self) -> np.ndarray:
        self.current_index = 0

        if not self.emails:
            self.current_email = None
        else:
            self.current_email = self.emails[self.current_index]

        return self._get_observation()

    def step(self, action: int) -> Tuple[np.ndarray, float, bool, dict]:
        done = False
        info = {}

        if self.current_email is None:
            return self._get_observation(), 0.0, True, info

        email = self.current_email

        # Task completion logic
        task_completed = False
        if action == 3 and email.tasks:
            email.tasks[0].completed = True
            task_completed = True

        reward = self.grader.grade(task_completed)

        # Move to next email
        self.current_index += 1

        if self.current_index >= len(self.emails):
            done = True
            self.current_email = None
        else:
            self.current_email = self.emails[self.current_index]

        return self._get_observation(), reward, done, info

    def _get_observation(self) -> np.ndarray:
        if self.current_email is None:
            return np.array([0, 0], dtype=np.float32)

        task_count = len(self.current_email.tasks)

        first_priority = (
            self.current_email.tasks[0].priority
            if task_count > 0
            else 0
        )

        return np.array([task_count, first_priority], dtype=np.float32)

    def render(self, mode="human"):
        if self.current_email:
            print(
                f"Email: {self.current_email.subject} | "
                f"Tasks: {len(self.current_email.tasks)}"
            )
        else:
            print("No more emails.")