import matplotlib.pyplot as plt 
import matplotlib.patches   

circle = plt.Circle((2,2), radius = 1, color = 'green')
rectangle = plt.Rectangle((3,3), width = 2, height = 1, facecolor = 'yellow', edgecolor = 'black')
line = plt.Line2D((0,5) ,(5,5), color = 'purple')  

ax = plt.gca()
print("ax: ", ax)
print("type(ax): ", type(ax))

ax.add_patch(circle)
ax.add_patch(rectangle)
ax.add_line(line)

plt.axis('scaled')
plt.axis('off')
plt.show()