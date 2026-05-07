import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# parameters
N = 30      # number of molecules
L = 10      # box size
r = 0.3     # molecule radius
m = 1       # molecule mass
dt = 0.1    # time step

# initial positions and velocities
positions = np.random.rand(N, 3) * (L - 2 * r) + r  
velocities = (np.random.randn(N, 3)) * 4            

kinetic_energies = []

# plot setup
plt.style.use('dark_background')
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(
    positions[:, 0], positions[:, 1], positions[:, 2],
    s=120, c='lime', edgecolors='black', linewidths=1.5, alpha=0.85
)

# axes and grid setup
for spine in ax.spines.values():
    spine.set_edgecolor('gray')
ax.set_facecolor('#181818')
ax.grid(color='#444444', linestyle=':', linewidth=0.7, alpha=0.5)

ax.set_xlim([0, L])
ax.set_ylim([0, L])
ax.set_zlim([0, L])
ax.set_box_aspect([1, 1, 1])
ax.set_title("3D Kinetic Gas Theory Model", color='white', fontsize=18, fontweight='bold', pad=20)

# draw_box function to create a 3D box
def draw_box(ax, L, color='#555', lw=2, alpha=0.7):
    for s, e in [
    
        ([0, 0, 0], [L, 0, 0]), ([L, 0, 0], [L, L, 0]), ([L, L, 0], [0, L, 0]), ([0, L, 0], [0, 0, 0]),
        ([0, 0, L], [L, 0, L]), ([L, 0, L], [L, L, L]), ([L, L, L], [0, L, L]), ([0, L, L], [0, 0, L]),
        ([0, 0, 0], [0, 0, L]), ([L, 0, 0], [L, 0, L]), ([L, L, 0], [L, L, L]), ([0, L, 0], [0, L, L])
    ]:
        ax.plot3D(*zip(s, e), color=color, lw=lw, alpha=alpha)

draw_box(ax, L)

# update function for animation
def update(frame):
    global positions, velocities

    # update positions
    positions[:] += velocities * dt

    # wall collisions
    for dim in range(3):
        mask_low = positions[:, dim] < r
        mask_high = positions[:, dim] > (L - r)
        velocities[mask_low, dim] *= -1
        velocities[mask_high, dim] *= -1
        positions[mask_low, dim] = r
        positions[mask_high, dim] = L - r

    # kinetic energy calculation
    ke = 0.5 * m * np.sum(velocities**2, axis=1)
    kinetic_energies.append(np.mean(ke))

    # scatter update
    sc._offsets3d = (positions[:, 0], positions[:, 1], positions[:, 2])
    sc.set_facecolor('lime')
    sc.set_edgecolor('black')
    sc.set_alpha(0.85)
    sc.set_sizes(np.full(N, 120 + 40 * np.sin(frame * 0.1)))  # pulsing

    # adding a glow effect
    ax.scatter(
        positions[:, 0], positions[:, 1], positions[:, 2],
        s=400, c='lime', alpha=0.07, marker='o', zorder=0
    )

    return sc,

ani = FuncAnimation(fig, update, frames=300, interval=50, blit=False)
plt.show()


# --- Scientific background ---
# This simulation visualizes the kinetic theory of gases in three dimensions.
# Each sphere represents a gas molecule moving inside a cubic box, bouncing off the walls.
# The random initial velocities mimic the thermal motion of molecules at a given temperature.
# As the simulation runs, you can observe:
#   - Molecules move in straight lines between collisions.
#   - When a molecule hits a wall, it bounces back, reversing the velocity component perpendicular to the wall.
#   - The average kinetic energy of the molecules is tracked, which is directly related to the temperature of the gas.
# According to the kinetic theory, the pressure exerted by a gas on the walls of its container arises from these collisions.
# The distribution of molecular speeds and energies follows the Maxwell–Boltzmann distribution.
# This model helps explain macroscopic gas laws (like PV = nRT) from microscopic particle behavior.