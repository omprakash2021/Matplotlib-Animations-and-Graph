import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle as rect
from matplotlib.patches import RegularPolygon as poly 

fig, ax = plt.subplots()

rect1 = rect((1, 1), 4, 2, rotation_point='center', color='orange')
ax.add_patch(rect1)

rect1.set_angle(10)
plt.grid()
plt.axis('scaled')
plt.show()