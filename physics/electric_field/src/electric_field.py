import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# columb's constant (in N m²/C²)
k = 1

# create a grid of points in the 2D plane
x = np.linspace(-5, 5, 32)   
y = np.linspace(-5, 5, 32)   
X, Y = np.meshgrid(x, y)     

# time steps for the animation
t_vals = np.linspace(0.2 * np.pi, 200)  

# charge value (can be positive or negative)
q = 1

def electric_field(q, r0, X, Y):
    """
    Calculate the electric field vector (Ex, Ey) produced by a point charge q at position r0.

    Parameters:
        q (float): charge value (can be positive or negative)
        r0 (list or array): position of the charge [x0, y0]
        X, Y (2D arrays): grid of points where the field is calculated

    Returns:
        Ex, Ey (2D arrays): components of the electric field at each grid point
    """
    rx = X - r0[0]  # x-distance from charge to each grid point
    ry = Y - r0[1]  # y-distance from charge to each grid point
    r_squared = rx**2 + ry**2  # squared distance from charge to each grid point
    E = k * q / r_squared      # electric field magnitude (Coulomb's law)
    Ex = E * rx / np.sqrt(r_squared)  # x-component (directional)
    Ey = E * ry / np.sqrt(r_squared)  # y-component (directional)
    return Ex, Ey

# plot setup
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_facecolor("black")

# field vectors initialization
Ex, Ey = np.zeros_like(X), np.zeros_like(Y)
color = np.zeros_like(X)

# quiver plot for electric field vectors
quiver = ax.quiver(
    X, Y, Ex, Ey, color,
    cmap='hsv', scale=50, pivot='middle', clim=[0, 2 * np.pi]
)

# plot for the charges
charge1 = ax.plot([], [], 'ro', markersize=12)[0]
charge2 = ax.plot([], [], 'bo', markersize=12)[0]

def update(frame):
    """
    Update function for the animation.
    Moves the charges in a circular path and updates the electric field vectors.
    """
    t = t_vals[frame]
    # move the charges in a circular path
    r1 = [2 * np.cos(t), 2 * np.sin(t)]     # positive charge
    r2 = [-2 * np.cos(t), -2 * np.sin(t)]   # negative charge

    # calculate the electric field at each grid point
    Ex1, Ey1 = electric_field(q, r1, X, Y)
    Ex2, Ey2 = electric_field(-q, r2, X, Y)
    Ex = Ex1 + Ex2
    Ey = Ey1 + Ey2

    # color based on the angle of the electric field vector
    angle = np.arctan2(Ey, Ex) % (2 * np.pi)

    # update the quiver plot and charge positions
    quiver.set_UVC(Ex, Ey, angle)
    charge1.set_data([r1[0]], [r1[1]])
    charge2.set_data([r2[0]], [r2[1]])
    return quiver, charge1, charge2

# animation setup
ani = FuncAnimation(fig, update, frames=len(t_vals), blit=False, interval=50)
plt.show()

# --- Scientific background ---
# This simulation shows the electric field created by two point charges: one positive and one negative, both with the same magnitude.
# The charges move in a circle, always opposite each other. At every step of the animation, the electric field is recalculated for every point on the grid.
# According to Coulomb's law, the electric field E from a point charge q at position r0 is:
#     E = k * q / r^2
# where r is the distance from the charge to the point where we're measuring the field, and k is Coulomb's constant.
# The field points away from positive charges and toward negative ones.
# What you see on the plot is the combined effect of both charges: at each point, the field vectors from both charges are added together.
# The color of each arrow shows the direction of the field at that spot, making it easier to see the overall pattern and how it changes as the charges move.