import gym
import gym_jsbsim
import os

env = gym.make('JSBSim-TurnHeadingControlTask-F16-Shaping.STANDARD-FG-v0')

env.reset()
done = False

while True:
   action = env.action_space.sample()
   state, reward, done, _ = env.step(action)
   env.render(mode='flightgear')