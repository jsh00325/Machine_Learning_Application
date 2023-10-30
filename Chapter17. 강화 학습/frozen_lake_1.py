import gym

env = gym.make("FrozenLake-v1", render_mode='human', is_slippery=False)
print(env.observation_space.n)
print(env.action_space.n)
env.reset()

n=30
env.render()				
for i in range(n):
  action = env.action_space.sample()
  state, reward, done, truncated, info = env.step(action)
  print(f"({action}, {state}, {reward})", end="->")
  env.render()
  if done: break

env.close()