
import os
import gym
from stable_baselines3 import PPO as Algorithm

SAVENAME  = "PPOv2" # should contain the algorithm

SAVE_REPLAY = True

if SAVE_REPLAY:
    from save_image_to import save_images_as_animation
    SCREENSHOT_PATH = f"screenshots/{SAVENAME}"

    if not os.path.exists(SCREENSHOT_PATH):
        os.makedirs(SCREENSHOT_PATH)
        
        

env = gym.make("LunarLander-v2")
env.reset()

model_file = "2990000"
models_dir = f"models/{SAVENAME}"
model_path = f"{models_dir}/{model_file}"

model = Algorithm.load(model_path, env=env)

episodes = 10
frames = []
for ep in range(episodes):
    obs = env.reset()
    done = False    
    
    while not done:
        if SAVE_REPLAY:
            frames.append(env.render(mode="rgb_array"))
        else:
            env.render()
              
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(action)

if SAVE_REPLAY:        
    save_images_as_animation(frames, f"{SCREENSHOT_PATH}/anim.gif")
        
#    save_frames_as_gif(frames, SCREENSHOT_PATH)
        
env.close()