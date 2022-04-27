import os
import gym
from stable_baselines3 import DQN as Algorithm


# Config
TIMESTEPS = 10_000  # save every n steps

SAVENAME  = "DQNv1" # should contain the algorithm

models_dir = f"models/{SAVENAME}"
logdir = "logs"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)
    
if not os.path.exists(logdir):
    os.makedirs(logdir)

env = gym.make("LunarLander-v2")
env.reset()


model = Algorithm("MlpPolicy", env, verbose=1, tensorboard_log=logdir)

for i in range(1,30):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=SAVENAME)
    model.save(f"{models_dir}/{TIMESTEPS*i}")
    
    
    
    
        
env.close()