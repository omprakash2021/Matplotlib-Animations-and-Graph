#Reference:
#[1]: https://scales.arabpsychology.com/stats/how-to-draw-rectangles-in-matplotlib-with-examples/
#[2]: https://stackoverflow.com/questions/4285103/matplotlib-rotating-a-patch
#[3]: https://www.w3schools.com/python/matplotlib_markers.asp
#[4]: https://www.scaler.com/topics/matplotlib/plot-shape-matplotlib/
#[5]: https://www.scaler.com/topics/matplotlib/matplotlib-set-axis-range/

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as rect
from matplotlib.patches import RegularPolygon as regularPoly
from functools import partial
from matplotlib.animation import FuncAnimation as animation
import numpy as np
import time 
import sys
print(sys.executable)
fig, ax = plt.subplots(figsize = (12, 12))

#(bottom left position), width, height
rect1 = rect((-2, -1), 4, 2, rotation_point='center', color='orange')
ax.add_patch(rect1)

tri1 = regularPoly((0, 0), numVertices=3, radius=1, fc='red', ec='black')
ax.add_patch(tri1)

ax.plot(0, 0, marker='o', markersize = 5, markerfacecolor='green', markeredgecolor = 'white')
ax.plot(0, 0, marker='o', markersize = 5, markerfacecolor='green', markeredgecolor = 'white')


ax.set_xlim(-np.pi * 2, np.pi * 2)
ax.set_ylim(-np.pi * 2, np.pi * 2)
ax.axhline(y = 0.0, color = 'r', linestyle = '-') 
ax.axvline(x = 0.0, color = 'r', linestyle = '-') 

print(tri1.get_path())

def update(rect1, tri1, frame):
    # rect1.set_angle(frame*180/np.pi)
    # tri1.orientation = (frame * 180/np.pi)
    # print(f"deg: {(frame * 180/np.pi): .2f}")
    # print(tri1.get_path())
    tri1.orientation = 10
    time.sleep(3)
    tri1.orientation = 10
    time.sleep(3)
    tri1.orientation = 10
    time.sleep(3)
    tri1.orientation = 10
    time.sleep(3)
    tri1.orientation = 10
    time.sleep(3)
    tri1.orientation = 10
    time.sleep(3)
    tri1.orientation = 10
    time.sleep(3)
    tri1.orientation = 10
    time.sleep(3)
    tri1.orientation = 10
    time.sleep(3)
    return tri1,

animate = animation(fig, partial(update, rect1, tri1), frames=np.linspace(0, 2*np.pi, 2000), blit=True, interval=800)

# plt.axis('scaled')
# fig.tight_layout()
plt.gca().set_aspect('equal', adjustable='box')
plt.grid()
plt.show()