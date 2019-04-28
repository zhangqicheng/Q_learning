from maze_env import Maze
from RL_brain import QLearningTable


def update():
    for episode in range(100):
        # 初始化，得到一个刚开始的四维信息x1,y1,x2,y2
        observation = env.reset()

        while True:
            # 更新可视化环境，虽然我不懂啥意思
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.move(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break

    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()