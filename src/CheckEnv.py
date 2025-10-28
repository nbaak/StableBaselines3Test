from stable_baselines3.common.env_checker import check_env
import gym

env = gym.make("LunarLander-v2")
# It will check your custom environment and output additional warnings if needed


check_env(env)