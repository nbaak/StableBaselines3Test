import gymnasium as gym
from stable_baselines3 import PPO

def main() -> None:
    # Gymnasium environment
    env = gym.make("CartPole-v1", render_mode="human")

    # SB3 PPO with vectorized env handled internally
    model = PPO("MlpPolicy", env, verbose=0)
    model.learn(total_timesteps=10_000)

    # Normal loop — Gymnasium v1 API
    obs, _ = env.reset()
    for _ in range(1000):
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, terminated, truncated, info = env.step(action)
        env.render()
        if terminated or truncated:
            obs, _ = env.reset()

    env.close()

if __name__ == "__main__":
    main()
