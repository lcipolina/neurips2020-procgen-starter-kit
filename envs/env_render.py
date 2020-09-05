import gym
import gym.wrappers

env = gym.make("procgen:procgen-coinrun-v0", render_mode="rgb_array")
env.metadata["render.modes"] = ["human", "rgb_array"]
env = gym.wrappers.Monitor(env=env, directory="./videos", force=True)

episodes = 10
_ = env.reset()

done = False
while episodes > 0:
    _, _, done, _ = env.step(env.action_space.sample())
    if done:
        _ = env.reset()
        episodes -= 1