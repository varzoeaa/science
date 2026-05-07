import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# parameters
N = 40          # number of molecules
L0 = 8          # initial box size (edge length)
T0 = 300        # initial temperature (K)
m = 1           # molecule mass (arbitrary units)
k = 1           # boltzmann constant (scaled for visualization)
dt = 0.05       # time step
r = 0.2         # molecule radius

# initial
positions = np.random.rand(N, 3) * (L0 - 2*r) + r 
velocities = np.random.randn(N, 3)
velocities *= np.sqrt(k * T0 / m) / np.std(velocities)  

# fig and axes setup
plt.style.use('dark_background')
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.22)

# sliders
axcolor = 'gray'
ax_L = plt.axes([0.15, 0.10, 0.7, 0.03], facecolor=axcolor)
ax_T = plt.axes([0.15, 0.05, 0.7, 0.03], facecolor=axcolor)
slider_L = Slider(ax_L, 'Volume (V)', 4, 12, valinit=L0, valstep=0.1)
slider_T = Slider(ax_T, 'Temperature (T)', 100, 600, valinit=T0, valstep=1)

# draw box
def draw_box(ax, L, color='#888', lw=2, alpha=1.0):
    for s, e in [
        ([0, 0, 0], [L, 0, 0]), ([L, 0, 0], [L, L, 0]), ([L, L, 0], [0, L, 0]), ([0, L, 0], [0, 0, 0]),
        ([0, 0, L], [L, 0, L]), ([L, 0, L], [L, L, L]), ([L, L, L], [0, L, L]), ([0, L, L], [0, 0, L]),
        ([0, 0, 0], [0, 0, L]), ([L, 0, 0], [L, 0, L]), ([L, L, 0], [L, L, L]), ([0, L, 0], [0, L, L])
    ]:
        ax.plot3D(*zip(s, e), color=color, lw=lw, alpha=alpha)

# scatter plot for molecules
sc = ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], s=60, c='lime', edgecolors='black', alpha=0.9)

# text annotations
pressure_text = ax.text2D(0.05, 0.92, '', transform=ax.transAxes, fontsize=16, color='orange', fontweight='bold')
formula_text = ax.text2D(0.5, 1.02, r"$pV = nRT$", transform=ax.transAxes, fontsize=18, color='white', ha='center')

# update function for animation
wall_hits = 0
t = 0
prev_T = T0  # store previous temperature for velocity rescaling

def update(frame):
    global positions, velocities, wall_hits, t, prev_T
    L = slider_L.val
    T = slider_T.val
    n = N / 6.022e23  # number of moles (for reference, not used directly)
    t += dt

    # only rescale velocities if temperature has changed
    if T != prev_T:
        velocities[:] *= np.sqrt(T / prev_T)
        prev_T = T

    # update positions
    positions[:] += velocities * dt

    # wall collisions
    for i in range(N):
        for j in range(3):
            if positions[i, j] < r:
                positions[i, j] = r
                velocities[i, j] *= -1
                wall_hits += 1
            elif positions[i, j] > L - r:
                positions[i, j] = L - r
                velocities[i, j] *= -1
                wall_hits += 1

    # clear and redraw the plot
    ax.cla()
    ax.set_xlim([0, L])
    ax.set_ylim([0, L])
    ax.set_zlim([0, L])
    ax.set_box_aspect([1, 1, 1])      
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    draw_box(ax, L)
    sc = ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], s=60, c='lime', edgecolors='black', alpha=0.9)

    # calculate pressure
    elapsed = t if t > 0 else 1
    pressure = wall_hits / elapsed / (6 * L * L)  # 6 walls, area L^2 each
    pressure_text = ax.text2D(0.05, 0.92, f"Pressure: {pressure:.3f} (arb. units)", transform=ax.transAxes, fontsize=16, color='orange', fontweight='bold')
    formula_text = ax.text2D(0.5, 1.02, r"$pV = nRT$", transform=ax.transAxes, fontsize=18, color='white', ha='center')

    return sc, pressure_text, formula_text

ani = FuncAnimation(fig, update, frames=500, interval=30, blit=False)
plt.show()

# --- Scientific background ---
# This interactive simulation visualizes the ideal gas law (PV = nRT) at the microscopic level.
# Each green dot represents a gas molecule moving freely inside a cubic box, bouncing elastically off the walls.
# You can change the volume (box size) and temperature using the sliders:
#   - Increasing the temperature increases the average speed of the molecules.
#   - Decreasing the volume increases the frequency of wall collisions.
# The pressure is estimated by counting wall collisions per unit time and area, showing how microscopic motion leads to macroscopic pressure.
# The ideal gas law connects pressure (p), volume (V), temperature (T), and the number of particles (n), and this model demonstrates how these quantities are related through molecular motion.
# This approach helps bridge the gap between the microscopic world of particles and the macroscopic behavior described by thermodynamics.