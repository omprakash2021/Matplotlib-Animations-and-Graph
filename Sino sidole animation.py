import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
x_data = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x_data, np.sin(x_data))

# Function to update the plot for each animation frame
def update(frame):
    line.set_ydata(np.sin(x_data + frame / 10))  # Example: animate the sine wave
    return line,

# Create the animation
animation = FuncAnimation(fig, update, frames=range(200), interval=50)

plt.show()
