import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parameters ---
p = np.linspace(0, 100, 400)  # Pressure axis (arbitrary units)
T = 1.0                       # Fixed reduced temperature (Tr = T/Tc)
a = 1.0                       # Attraction parameter (arbitrary units)
b = 0.1                       # Repulsion parameter (arbitrary units)
R = 1.0                       # Gas constant (scaled)

def Z_vdw(p, T):
    # Simplified van der Waals compressibility factor
    return 1 / (1 - b * p / (R * T)) - a * p / (R**2 * T**2)

Z = Z_vdw(p, T)

# --- Figure setup ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 100)
ax.set_ylim(-200, 100)
ax.set_xlabel("Pressure (p)", color='white', fontsize=14)
ax.set_ylabel("Compressibility Factor (Z)", color='white', fontsize=14)
ax.set_title(f"Z vs p at T = {T} (van der Waals Gas)", color='white', fontsize=18, pad=15)
ax.tick_params(colors='white')
ax.grid(color='#444', linestyle=':', linewidth=0.7, alpha=0.5)

# --- Plot the Z-p curve ---
curve, = ax.plot(p, Z, color='cyan', lw=2, label='Z(p)')
# --- Plot the ideal gas line ---
ax.plot(p, np.ones_like(p), color='gray', lw=2, linestyle='--', label='Ideal Gas (Z=1)')

# --- Moving point (animated) ---
point, = ax.plot([], [], 'o', color='orange', markersize=12)

# --- Animation update function ---
def update(frame):
    idx = frame % len(p)  # Loop over p
    px = p[idx]
    zx = Z[idx]
    # Color and size encode pressure
    color = plt.cm.plasma(idx / len(p))
    size = 12 + 18 * (idx / len(p))
    point.set_data([px], [zx])
    point.set_color(color)
    point.set_markersize(size)
    return point,

ani = FuncAnimation(fig, update, frames=len(p), interval=20, blit=True, repeat=True)
ax.legend(loc='upper left', fontsize=12, frameon=False)
plt.tight_layout()
plt.show()

# --- Scientific background ---
# This animation shows how the compressibility factor Z = pV/(nRT) of a real gas changes with pressure at a fixed temperature.
# For an ideal gas, Z = 1 (gray dashed line). For a real gas, Z deviates from 1 due to molecular interactions.
# As pressure increases, the orange point moves along the Z–p curve, with its color and size encoding the current pressure.
# This helps visualize how real gases become less ideal at high pressures, and how Z reflects the balance of attractive and repulsive forces.