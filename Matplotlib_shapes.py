import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse
from matplotlib.patches import RegularPolygon
from matplotlib.patches import Polygon

fig, ax = plt.subplots()
ax.axis([0, 20, 0, 20]) #ax.xlim, ax.ylim

# shape1 = Rectangle((5, 5), width=10, height=5, angle=0, fill = False, color='Red')
# shape2 = Circle((10, 10), radius = 5, fill = False, edgecolor = 'Red')
# shape3 = Ellipse((10, 10), width = 10, height = 5, angle = 0, color = 'Green')
# shape4 = RegularPolygon((10, 10), numVertices = 3, radius = 5, facecolor = 'purple', edgecolor = 'blue')
# shape4 = RegularPolygon((10, 10), numVertices = 5, radius = 5, facecolor = 'purple', edgecolor = 'blue')

array = np.array([(2,2), (2, 8), (6, 12), (10, 8), (10, 2)])
shape5 = Polygon(array)

# ax.add_patch(shape1)
# ax.add_patch(shape2)
# ax.add_patch(shape3)
# ax.add_patch(shape4)
ax.add_patch(shape5)

plt.show()