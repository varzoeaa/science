import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# energy range
E = np.linspace(0, 5, 200)  

# boltzmann distribution function
def boltzmann(E, T):
    """
    Returns the relative number of particles at energy E for a given temperature T
    according to the Boltzmann distribution (normalized for visualization).
    """
    return np.exp(-E / T)

# figure setup
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 5)
ax.set_ylim(0, 1.05)
ax.set_xlabel("Energy (E)", color='white')
ax.set_ylabel("Relative number of particles", color='white')
ax.set_title("Boltzmann Distribution", color='white', fontsize=18, pad=15)
ax.tick_params(colors='white')
ax.grid(color='#444', linestyle=':', linewidth=0.7, alpha=0.5)

# plot setup
line, = ax.plot([], [], lw=3, color='cyan', alpha=0.95, zorder=10)
glow, = ax.plot([], [], lw=12, color='cyan', alpha=0.08, zorder=5)
temp_text = ax.text(0.05, 0.92, '', transform=ax.transAxes, fontsize=15, color='orange', fontweight='bold')

# update function for animation
def update(frame):
    # temperature increases with each frame
    T = 0.5 + frame * 0.05
    # calculating for the current temperature
    f_E = boltzmann(E, T)
    # max layer is normalized for visualization
    f_E /= f_E.max()
    # updating plots
    line.set_data(E, f_E)
    glow.set_data(E, f_E)
    temp_text.set_text(f"Temperature: {T:.2f}")
    return line, glow, temp_text


ani = FuncAnimation(fig, update, frames=50, interval=100, blit=True)
plt.tight_layout()
plt.show()

# --- Scientific background ---
# The Boltzmann distribution describes how particles in a system are distributed among different energy levels at a given temperature.
# At low temperatures, most particles have low energy, so the curve is steep and falls off quickly.
# As the temperature increases, the distribution "flattens out": more particles have higher energy, and the curve becomes broader.
# This animation shows how the shape of the Boltzmann distribution changes as temperature rises.
# The area under the curve represents the total number of particles (here, the curve is normalized for visualization).
# The Boltzmann distribution is fundamental in statistical mechanics and explains phenomena such as evaporation, chemical reaction rates, and the behavior of gases.