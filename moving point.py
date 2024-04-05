import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

def f(x):
    return 0.25*(x+4)*(x+1)*(x-2)

x_range = np.linspace(-4, 4, 1000)

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 25)
ax.set_title('My function')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.annotate('Minimum', xy = (-1, 1.8), xytext = (-1, 4), arrowprops = {})

line, = ax.plot(x_range, f(x_range), lw = 2)

point, = ax.plot([], [], 'bo', markersize = 10)

def animate(i):
    # print("frame: ", i)
    x = x_range[i]
    y = f(x)
    point.set_data(x, y)
    return point, line

anim = animation.FuncAnimation(fig, animate, frames = len(x_range), interval = 20)

# writervideo = animation.FFMpegWriter(fps = 60)
# anim.save('Function.mp4', writer = writervideo)

plt.show()