import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# --- Parameters ---
T = np.linspace(100, 600, 60)   # Temperature axis (K)
V = np.linspace(1, 20, 60)      # Volume axis (arbitrary units)
TT, VV = np.meshgrid(T, V)

# van der Waals parameters (arbitrary units)
a = 1.0
b = 0.5
R = 1.0
n = 1.0

# Internal energy for van der Waals gas:
# U = (3/2) nRT - a n^2 / V
U = (3/2) * n * R * TT - a * n**2 / VV

# --- 3D Surface Plot setup ---
plt.style.use('dark_background')
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = [ax.plot_surface(TT, VV, U, cmap='hot', edgecolor='none', alpha=0.92)]

ax.set_xlabel('Temperature (T)', color='white', fontsize=12)
ax.set_ylabel('Volume (V)', color='white', fontsize=12)
ax.set_zlabel('Internal Energy (U)', color='white', fontsize=12)
ax.set_title('Internal Energy U(T, V) for a van der Waals Gas', color='white', fontsize=16, pad=18)
ax.tick_params(colors='white')

fig.colorbar(surf[0], ax=ax, shrink=0.5, aspect=10, label='U', pad=0.1)

# --- Animation: rotate the camera around the surface ---
def update(frame):
    ax.view_init(elev=30, azim=frame)
    return surf

ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=60, blit=False)
plt.tight_layout()
plt.show()

# --- Scientific background ---
# This animation shows the internal energy (U) of a real gas as a function of temperature (T) and volume (V).
# For an ideal gas, U depends only on T, but for a van der Waals gas, U also depends on V due to intermolecular attractions (the -a/V term).
# The surface plot and its rotation help visualize how both temperature and volume influence the internal energy of a real gas.
