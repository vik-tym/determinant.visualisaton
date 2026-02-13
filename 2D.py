import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from IPython.display import Image  # для показу GIF у ноутбуку


v1 = np.array([2, 1])
v2 = np.array([1, 2])
vectors = np.column_stack([v1, v2])

A = np.array([[1, 2],
              [0.5, 1]])

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 6)
ax.set_aspect('equal')
ax.grid(True)

poly = plt.Polygon([[0,0],[0,0],[0,0],[0,0]], color='orange', alpha=0.5)
ax.add_patch(poly)

def update(frame):
    t = frame/50
    M = np.eye(2)*(1-t) + A*t
    new_vectors = M @ vectors
    points = np.array([[0,0], new_vectors[:,0], new_vectors[:,0]+new_vectors[:,1], new_vectors[:,1]])
    poly.set_xy(np.vstack([points, points[0]]))
    return poly,

ani = FuncAnimation(fig, update, frames=51, blit=True)


ani.save("parallelogram.gif", writer=PillowWriter(fps=10))


Image(filename="parallelogram.gif")