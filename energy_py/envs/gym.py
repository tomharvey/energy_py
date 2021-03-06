import random

import gym
import numpy as np

from energy_py.common import GlobalSpace, DiscreteSpace, ContinuousSpace


class EnvWrapper(object):

    def __init__(self, env):
        self.env = env

    def __repr__(self):
        return repr(self.env)

    def step(self, action):
        return self.env.step(action)

    def reset(self):
        return self.env.reset()

    def seed(self, seed=None):
        if seed:
            return self.env.seed(int(seed))


class CartPoleEnv(EnvWrapper):

    def __init__(self):
        env = gym.make('CartPole-v0')
        super(CartPoleEnv, self).__init__(env)

        self.observation_space = self.env.observation_space

        self.action_space = GlobalSpace('action').from_spaces(
            DiscreteSpace(2), 'push_l_or_r'
        )

    def step(self, action):
        #  doesn't accept an array!
        return self.env.step(action[0][0])


class PendulumEnv(EnvWrapper):

    def __init__(self):
        env = gym.make('Pendulum-v0')
        super(PendulumEnv, self).__init__(env)

        self.observation_space = GlobalSpace('observation').from_spaces(
            ContinuousSpace(low=-env.max_torque, high=env.max_torque)
        )


class MountainCarEnv(EnvWrapper):

    def __init__(self):
        env = gym.make('MountainCar-v0')
        super(MountainCarEnv, self).__init__(env)

        self.observation_space = self.env.observation_space

        self.action_space = GlobalSpace('action').from_spaces(
            DiscreteSpace(2), 'push_l_or_r'
        )

    def step(self, action):
        #  doesn't accept an array!
        return self.env.step(action[0][0])
