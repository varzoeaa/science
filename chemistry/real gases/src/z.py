import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parameters for the plot ---
p = np.linspace(0, 100, 400)  # Pressure axis (arbitrary units)
T_list = [0.8, 1.0, 1.2, 1.5, 2.0]  # Different reduced temperatures (Tr = T/Tc)
colors = ['red', 'orange', 'lime', 'cyan', 'magenta']  # Colors for each isotherm

# --- Compressibility factor Z for a van der Waals gas (simplified) ---
# Z = pV/(nRT), for real gases Z ≠ 1
# Here we use a simple van der Waals-like model for demonstration:
a = 1.0  # Attraction parameter (arbitrary units)
b = 0.1  # Repulsion parameter (arbitrary units)
R = 1.0  # Gas constant (scaled)

def Z_vdw(p, T):
    # Z = 1 / (1 - b*p/(R*T)) - a*p/(R**2*T**2)
    return 1 / (1 - b * p / (R * T)) - a * p / (R**2 * T**2)

# --- Figure setup ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 100)
ax.set_ylim(-100, 100)
ax.set_xlabel("Pressure (p)", color='white', fontsize=14)
ax.set_ylabel("Compressibility Factor (Z)", color='white', fontsize=14)
ax.set_title("Z vs p Isotherms (Compressibility Dance)", color='white', fontsize=18, pad=15)
ax.tick_params(colors='white')
ax.grid(color='#444', linestyle=':', linewidth=0.7, alpha=0.5)

# --- Plot the ideal gas line (Z=1) ---
ideal_line, = ax.plot(p, np.ones_like(p), color='white', lw=3, label='Ideal Gas (Z=1)', zorder=10)

# --- Prepare lines for each isotherm ---
lines = []
for color, T in zip(colors, T_list):
    line, = ax.plot([], [], color=color, lw=2, label=f"T = {T}")
    lines.append(line)

# --- Legend ---
ax.legend(loc='upper left', fontsize=12, frameon=False)

# --- Animation update function ---
def update(frame):
    # Animate from left to right along the pressure axis
    p_anim = p[:frame]
    for i, T in enumerate(T_list):
        Z = Z_vdw(p_anim, T)
        lines[i].set_data(p_anim, Z)
    return lines

ani = FuncAnimation(fig, update, frames=len(p), interval=20, blit=True)
plt.tight_layout()
plt.show()

# --- Scientific background ---
# The compressibility factor Z = pV/(nRT) describes how much a real gas deviates from ideal gas behavior (Z=1).
# For an ideal gas, Z is always 1, regardless of pressure or temperature.
# For real gases, Z varies with pressure and temperature due to intermolecular forces and finite molecular size.
# At low pressures, all gases behave ideally (Z ≈ 1). At higher pressures, repulsive forces dominate (Z > 1).
# At intermediate pressures and low temperatures, attractive forces can make Z < 1.
# This animation shows Z vs p isotherms for several temperatures:
#   - The thick black line is the ideal gas (Z=1).
#   - Colored curves show real gas behavior at different temperatures.
#   - As temperature increases, the curves approach the ideal gas line.
# This visualization helps to understand the non-ideal behavior of real gases and the concept of compressibility.