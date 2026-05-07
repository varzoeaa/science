import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parameters ---
p = np.linspace(0.1, 100, 80)   # Pressure axis (avoid zero for stability)
T = np.linspace(0.5, 3.0, 60)   # Temperature axis
P, TT = np.meshgrid(p, T)

a = 1.0   # Attraction parameter (arbitrary units)
b = 0.1   # Repulsion parameter (arbitrary units)
R = 1.0   # Gas constant (scaled)

def Z_vdw(p, T):
    # Simplified van der Waals compressibility factor
    return 1 / (1 - b * p / (R * T)) - a * p / (R**2 * T**2)

Z = Z_vdw(P, TT)

# --- 3D Plot setup ---
plt.style.use('dark_background')
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = [ax.plot_surface(P, TT, Z, cmap='plasma', edgecolor='none', alpha=0.92)]

ax.set_xlabel('Pressure (p)', color='white', fontsize=12)
ax.set_ylabel('Temperature (T)', color='white', fontsize=12)
ax.set_zlabel('Compressibility Factor (Z)', color='white', fontsize=12)
ax.set_title('Z = f(p, T): Compressibility Surface', color='white', fontsize=16, pad=18)
ax.tick_params(colors='white')

# --- Animation: rotate the camera around the surface ---
def update(frame):
    ax.view_init(elev=30, azim=frame)
    return surf

ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), interval=60, blit=False)
plt.tight_layout()
plt.show()

# --- Scientific background ---
# This 3D surface shows how the compressibility factor Z = pV/(nRT) depends on both pressure (p) and temperature (T) for a real gas.
# For an ideal gas, Z = 1 everywhere. For real gases, Z deviates from 1 due to intermolecular forces.
# At low T and moderate p, Z < 1 (attraction dominates). At high p or high T, Z > 1 (repulsion dominates or ideal behavior is approached).
# This visualization helps you see the full landscape of real gas behavior as a function of both variables.