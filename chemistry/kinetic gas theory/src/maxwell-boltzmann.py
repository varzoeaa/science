import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# constants
k = 1.38e-23
m = 4.65e-26
v = np.linspace(0, 2000, 500)

# maxwell-boltzmann distribution formula
def maxwell_boltzmann(v, T):
    factor = (m / (2 * np.pi * k * T)) ** 1.5
    return 4 * np.pi * v**2 * factor * np.exp(-m * v**2 / (2 * k * T))

# setup the figure and axes
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#181818')
ax.set_facecolor('#222222')

ax.set_xlim(0, 2000)
ax.set_ylim(0, 0.0035000)
ax.spines['bottom'].set_color('#888')
ax.spines['top'].set_color('#888')
ax.spines['right'].set_color('#888')
ax.spines['left'].set_color('#888')
ax.tick_params(axis='x', colors='#aaa')
ax.tick_params(axis='y', colors='#aaa')

# grid
ax.grid(color='#444', linestyle=':', linewidth=0.7, alpha=0.5)

# line for the distribution curve
line, = ax.plot([], [], lw=3, color='lime', alpha=0.95, solid_capstyle='round', zorder=10)
glow, = ax.plot([], [], lw=12, color='lime', alpha=0.08, zorder=5)

# temperature text
temp_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=16, color='cyan', verticalalignment='top', fontweight='bold', zorder=20)

# title and labels
ax.set_title("Maxwell–Boltzmann Speed Distribution", color='white', fontsize=20, fontweight='bold', pad=20)
ax.set_xlabel("Speed (m/s)", color='white', fontsize=14)
ax.set_ylabel("Probability Density", color='white', fontsize=14)

# update function for animation
def update(frame):
    T = 100 + frame * 20  # temperature increases from 100 K upward
    f_v = maxwell_boltzmann(v, T)
    line.set_data(v, f_v)
    glow.set_data(v, f_v)
    temp_text.set_text(f"Temperature: {T} K")
    return line, glow, temp_text

anim = FuncAnimation(fig, update, frames=50, interval=100, blit=True)
plt.tight_layout()
plt.show()


# --- Scientific background ---
# The Maxwell–Boltzmann speed distribution describes how the speeds of particles in a gas are distributed at a given temperature.
# It is derived from statistical mechanics and applies to classical, non-quantum gases.
# At low temperatures, most particles move slowly, so the distribution is sharply peaked at low speeds.
# As the temperature increases, the distribution broadens and shifts to higher speeds: more particles move faster, and the most probable speed increases.
# The area under the curve represents the total number of particles (here, the curve is not normalized to 1, but the shape is correct).
# This distribution explains many macroscopic properties of gases, such as pressure and diffusion, and is fundamental to understanding thermal motion in physics and chemistry.