import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parameters ---
rows = 6
cols = 8
d = 1.0         # Distance between particles
Lx = (cols - 1) * d + 2
Ly = (rows - 1) * d + 2
r = 0.18        # Particle radius

# --- Generate grid of particles ---
def grid_positions(rows, cols, d, margin=1.0):
    x = np.linspace(margin, Lx - margin, cols)
    y = np.linspace(margin, Ly - margin, rows)
    X, Y = np.meshgrid(x, y)
    pos = np.vstack([X.ravel(), Y.ravel()]).T
    return pos

positions = grid_positions(rows, cols, d)

# --- Find neighbors for "springs" (bonds) ---
def neighbor_pairs(rows, cols):
    pairs = []
    for i in range(rows):
        for j in range(cols):
            idx = i * cols + j
            # Right neighbor
            if j < cols - 1:
                pairs.append((idx, idx + 1))
            # Down neighbor
            if i < rows - 1:
                pairs.append((idx, idx + cols))
    return pairs

bonds = neighbor_pairs(rows, cols)

# --- Figure setup ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, Lx)
ax.set_ylim(0, Ly)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
title = ax.set_title("Surface Tension: Molecular Model", color='white', fontsize=18, pad=15)

# --- Scatter plot for particles ---
sc = ax.scatter(positions[:, 0], positions[:, 1], s=350, c='#33aaff', edgecolors='black', zorder=10, alpha=0.95)

# --- Draw bonds as lines ---
lines = []
for i, j in bonds:
    line, = ax.plot([positions[i, 0], positions[j, 0]], [positions[i, 1], positions[j, 1]],
                    color='orange', lw=2.5, alpha=0.7, zorder=5)
    lines.append(line)

# --- Animation: stretch the top row (surface) ---
def update(frame):
    stretch = 0.0 + 0.7 * np.sin(frame * 0.07)
    new_pos = positions.copy()
    # Only move the top row (surface)
    top_idx = np.arange((rows - 1) * cols, rows * cols)
    new_pos[top_idx, 0] += stretch * (np.linspace(-1, 1, cols))
    # Update scatter
    sc.set_offsets(new_pos)
    # Update bonds
    for k, (i, j) in enumerate(bonds):
        xi, yi = new_pos[i]
        xj, yj = new_pos[j]
        lines[k].set_data([xi, xj], [yi, yj])
        # Highlight surface bonds
        if i in top_idx and j in top_idx:
            lines[k].set_color('yellow')
            lines[k].set_alpha(1.0)
            lines[k].set_linewidth(4)
        else:
            lines[k].set_color('orange')
            lines[k].set_alpha(0.7)
            lines[k].set_linewidth(2.5)
    # Title
    title.set_text("Surface Tension: Fewer bonds at the surface")
    return [sc, *lines, title]

ani = FuncAnimation(fig, update, frames=120, interval=60, blit=False)
plt.tight_layout()
plt.show()

# --- Scientific background ---
# This animation models surface tension at the molecular level.
# Inside the liquid, each molecule is surrounded by neighbors and experiences many attractive "bonds" (orange springs).
# At the surface, molecules have fewer neighbors, so fewer bonds pull them inward.
# When the surface is stretched, the top row molecules move apart, and you can see the reduced number of bonds at the surface (highlighted in yellow).
# This imbalance of forces at the surface is the microscopic origin of surface tension.