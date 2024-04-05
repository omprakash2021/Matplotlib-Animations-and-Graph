import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
fig.set_size_inches(700/100, 500/100)

x = np.linspace(0, 10, 100)
y = np.sin(x)

line, = ax.plot(x, y)
# line, = ax.plot(0, 0)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Sin Wave Animation')

def animate(frame):
    print("frame: ", frame)
    line.set_ydata(np.sin(x + frame/10))
    line.set_xdata(x)
    
    # line.set_ydata(np.sin(frame/10))
    # line.set_xdata(frame/10)

    return line,

fps = 30
frames = 300
animation = FuncAnimation(fig, animate, frames = frames, interval = 1000/fps, blit = True)
# animation.save('Sin Wave Animation using Matplotlib.mp4', writer = 'ffmpeg', fps = fps)
plt.show()