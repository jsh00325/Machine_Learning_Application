import gym
import numpy as np

env = gym.make("FrozenLake-v1",  is_slippery=False) 	# (1)

discount_factor = 0.9					# (2)
epsilon = 0.9
epsilon_decay_factor = 0.999
learning_rate = 0.8
num_episodes = 1000				# 1000번의 에피소드로 훈련

states = env.observation_space.n  		# 16
actions = env.action_space.n      		# 4
q_table = np.zeros((states, actions))		# (3)

for i in range(num_episodes):
    env.reset()
    state = 0
    epsilon *= epsilon_decay_factor	         # 입실론: 탐사와 활용 비율 결정
    done = False

    while not done:				# (4)
        if np.random.random() < epsilon:	# 난수가 입실론보다 작으면 탐사
            action = env.action_space.sample()	# 랜덤 액션
        else:					# 난수가 입실론보다 작으면 활용
            action = np.argmax(q_table[state])	# Q 테이블에서 가장 큰 값

        new_state, reward, done, truncated, info = env.step(action)
	 # 새로 얻은 정보로 Q-테이블 갱신
        q_table[state, action] +=   learning_rate * (reward + discount_factor * np.max(q_table[new_state]) - q_table[state, action])
        state = new_state
    print(f"{i}번째 에피소드 후 q table=")
    print(q_table)