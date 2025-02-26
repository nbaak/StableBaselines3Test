
import os
import gymnasium as gym
from stable_baselines3 import DQN as Algorithm

SAVENAME  = "DQNv1" # should contain the algorithm

SAVE_REPLAY = True

if SAVE_REPLAY:
    from save_image_to import save_images_as_animation
    SCREENSHOT_PATH = f"screenshots/{SAVENAME}"

    if not os.path.exists(SCREENSHOT_PATH):
        os.makedirs(SCREENSHOT_PATH)
        

env = gym.make("LunarLander-v3", render_mode="rgb_array")
env.reset()

model_file = "230000"
models_dir = f"models/{SAVENAME}"
model_path = f"{models_dir}/{model_file}"

model = Algorithm.load(model_path, env=env, verbose=1)

episodes = 10
frames = []
vec_env = model.get_env()

for ep in range(episodes):
    obs = vec_env.reset()
    done = False    
    
    while not done:
        if SAVE_REPLAY:
            frames.append(vec_env.render("rgb_array"))

        else:
            vec_env.render("human")
              
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, info = vec_env.step(action)

if SAVE_REPLAY:
    save_images_as_animation(frames, f"{SCREENSHOT_PATH}/anim.gif")
        
# save_frames_as_gif(frames, SCREENSHOT_PATH)
print("END")
env.close()
