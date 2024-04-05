import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_title('Point moving in Circular Path')
# ax.axis('equal')
ax.set_aspect('equal', 'box')
ax.axhline(y = 0, color = 'k')
ax.axvline(x = 0, color = 'k')
# point, = ax.plot(0, 0)
origin, = ax.plot(0, 0, 'ro', markersize = 5)
point, = ax.plot([], [], 'bo', markersize = 10)
radius, = ax.plot([0, 5], [0, 0], color = 'black')
path_x = [5, 5]
path_y = [0, 0]
track_path, = ax.plot(path_x, path_y, color = 'green')

def update(frame):
    # print("frame: ", frame)
    r = 5
    xdata = [np.cos(frame/10) * r]
    ydata = [np.sin(frame/10) * r]
    point.set_data(xdata, ydata)
    radius.set_data([0, xdata[0]], [0, ydata[0]])
    path_x.append(xdata[0])
    path_y.append(ydata[0])
    track_path.set_data(path_x, path_y)

    return point, origin, radius, track_path

frames = 500
animate = FuncAnimation(fig, update, frames = frames, interval = 100, blit = True)
plt.grid()
plt.show()