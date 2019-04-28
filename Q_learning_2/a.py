import tkinter as tk
import numpy as np
UNIT = 40   # pixels
MAZE_H = 4  # grid height
MAZE_W = 4  # grid width

root=tk.Tk()
canvas=tk.Canvas(bg='white',height=UNIT*MAZE_H,width=UNIT*MAZE_W)
for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            canvas.create_line(x0, y0, x1, y1)
for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            canvas.create_line(x0, y0, x1, y1)

origin = np.array([20, 20])
rect = canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red')
s=canvas.coords(rect)
actions=list(range(4))
print(actions)
canvas.pack()
root.mainloop()