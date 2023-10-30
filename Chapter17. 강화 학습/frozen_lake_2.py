import numpy as np
import gym

env = gym.make("FrozenLake-v1", is_slippery=False) # (1)

states = env.observation_space.n  		# = 16
actions = env.action_space.n      		# = 4
q_table = np.zeros((states, actions))

for i in range(200):
    env.reset()
    state = 0
    done = False

    while not done:
        if np.argmax(q_table[state]) > 0:
            action = np.argmax(q_table[state])
        else:					
            action = env.action_space.sample()

        new_state, reward, done, truncated, info = env.step(action)
        
        q_table[state, action] =  reward + np.max(q_table[new_state])
        state = new_state
    print(f"{i}번째 에피소드 후 q table=")
    print(q_table)
    env.render()