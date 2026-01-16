import numpy as np
import matplotlib.pyplot as plt

def draw_linear_map(ax, A, title):
    # ґратка
    x = np.linspace(-3, 3, 20)
    y = np.linspace(-3, 3, 20)

    for xi in x:
        pts = np.array([[xi, yi] for yi in y])
        pts_t = pts @ A.T
        ax.plot(pts_t[:, 0], pts_t[:, 1], color='lightgray')

    for yi in y:
        pts = np.array([[xi, yi] for xi in x])
        pts_t = pts @ A.T
        ax.plot(pts_t[:, 0], pts_t[:, 1], color='lightgray')

    # базис
    e1 = np.array([1, 0])
    e2 = np.array([0, 1])

    Ae1 = A @ e1
    Ae2 = A @ e2

    ax.quiver(0, 0, Ae1[0], Ae1[1],
              angles='xy', scale_units='xy', scale=1, color='red')
    ax.quiver(0, 0, Ae2[0], Ae2[1],
              angles='xy', scale_units='xy', scale=1, color='blue')

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_aspect('equal')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_title(title)

# Матриці
A_pos = np.array([[2, 1],
                  [1, 1]])     # det > 0

A_neg = np.array([[1, 2],
                  [2, 1]])     # det < 0

A_zero = np.array([[1, 1],
                   [2, 2]])    # det = 0

# Побудова
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

draw_linear_map(axes[0], A_pos, "det(A) > 0\nорієнтація збережена")
draw_linear_map(axes[1], A_neg, "det(A) < 0\nорієнтація змінена")
draw_linear_map(axes[2], A_zero, "det(A) = 0\nплощина → лінія")

plt.show()