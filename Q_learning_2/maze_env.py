import numpy as np
import time
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk
#基础属性
UNIT=40
MAZE_H=4
MAZE_W=4

#定义一个迷宫类
class Maze(tk.Tk,object):
    def __init__(self):
        super(Maze,self).__init__()
        self.action_space=[1,2,3,4]
        self.n_actions=len(self.action_space)
        self.title('Maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self._build_maze()

    #画迷宫
    def _build_maze(self):
        #生成一个160*160的画布
        self.canvas = tk.Canvas(self, bg='white',
                                height=MAZE_H * UNIT,
                                width=MAZE_W * UNIT)
        #画线
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        #这个不知道是干啥的
        origin = np.array([20, 20])

        #画两个地狱
        hell1_center = origin + np.array([UNIT * 2, UNIT])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 15, hell1_center[1] - 15,
            hell1_center[0] + 15, hell1_center[1] + 15,
            fill='black')
        hell2_center = origin + np.array([UNIT, UNIT * 2])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 15, hell2_center[1] - 15,
            hell2_center[0] + 15, hell2_center[1] + 15,
            fill='black')

        #画一个终点
        oval_center = origin + UNIT * 2
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 15, oval_center[1] + 15,
            fill='yellow')
        #画一个要运动的矩阵块
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red')

        # 全部显示到画布上
        self.canvas.pack()

    #初始化迷宫，恢复的和以前一样,返回小方块的四维信息x1,y1,x2,y2
    def reset(self):
        self.update()#进入事件循环
        time.sleep(0.5)
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red')
        return self.canvas.coords(self.rect)

    #小方块根据传入的方位进行移动，并返回下一个状态值，奖励，危险信息 s_,reward,done
    def move(self,action):
        s=self.canvas.coords(self.rect)  #获得小方块的列表状态信息
        base_action = np.array([0, 0])
        if action == 0:  # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:  # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:  # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:  # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])  # move agen
        s_=self.canvas.coords(self.rect)  #这里的位置已经移动，所以s_是移动的位置，不是原来的位置
        # reward function

        #如果成功到达目标
        if s_==self.canvas.coords(self.oval):
            reward=1
            done=True
            s_='terminal'
        elif s_ in [self.canvas.coords(self.hell1),self.canvas.coords(self.hell2)]:
            reward=-1
            done=True
            s_='terminal'
        else:
            reward=0
            done=False

        return s_,reward,done

    #这个函数不知道是干啥的，暂时不清楚
    def render(self):
        time.sleep(0.1)
        self.update()

#这是一个测试函数，用来测试哪里出现错误
def update():
    for t in range(10):
        s = env.reset()
        while True:
            env.render()
            a = 1
            s, r, done = env.move(a)
            if done:
                break

if __name__ == '__main__':
    env = Maze()
    env.after(100, update)
    env.mainloop()


