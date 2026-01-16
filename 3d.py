import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.animation import FuncAnimation, PillowWriter
from IPython.display import Image


def get_parallelepiped_verts(vectors):
    v1, v2, v3 = vectors.T
    origin = np.array([0,0,0])
    points = np.array([
        origin,
        v1,
        v2,
        v3,
        v1+v2,
        v1+v3,
        v2+v3,
        v1+v2+v3
    ])
    verts = [
        [points[0], points[1], points[4], points[2]], 
        [points[0], points[1], points[5], points[3]],
        [points[0], points[2], points[6], points[3]],
        [points[7], points[5], points[3], points[6]],
        [points[7], points[4], points[1], points[5]],
        [points[7], points[6], points[2], points[4]]
    ]
    return verts


v1 = np.array([1,0,0])
v2 = np.array([0,1,0])
v3 = np.array([0,0,1])
vectors = np.column_stack([v1, v2, v3])


A = np.array([[-2,0,0],[0,1,0],[0,0,1]])


fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-2,3)
ax.set_ylim(-2,3)
ax.set_zlim(-2,3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Паралелепіпед: det='+str(round(np.linalg.det(A),2)))


original_poly = Poly3DCollection(get_parallelepiped_verts(vectors), color='skyblue', alpha=0.3)
transformed_poly = Poly3DCollection(get_parallelepiped_verts(vectors), color='orange', alpha=0.5)
ax.add_collection3d(original_poly)
ax.add_collection3d(transformed_poly)


origin = np.array([0,0,0])
v_lines = [ax.quiver(*origin, *v, color=c, linewidth=2) for v,c in zip([v1,v2,v3], ['r','g','b'])]


def update(frame):
    t = frame / 50  # 0 -> 1
    M = np.eye(3)*(1-t) + A*t  
    transformed_vectors = M @ vectors
    transformed_poly.set_verts(get_parallelepiped_verts(transformed_vectors))
    return [transformed_poly]


ani = FuncAnimation(fig, update, frames=51, blit=True)


ani.save("parallelepiped_3D.gif", writer=PillowWriter(fps=10))


Image(filename="parallelepiped_3D.gif")