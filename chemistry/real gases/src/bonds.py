import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parameters ---
N = 18  # Number of particles
L = 8   # Box size
r = 0.3 # Particle radius

# Initial positions: random, but not too close to the walls
np.random.seed(42)
positions = np.random.rand(N, 2) * (L - 2*r) + r

# Choose interaction regime: "attractive" (Z<1) or "repulsive" (Z>1)
# You can switch between these for demonstration
interaction = "attractive"  # or "repulsive"

# --- Force calculation ---
def compute_forces(positions, regime):
    forces = np.zeros_like(positions)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            rij = positions[j] - positions[i]
            dist = np.linalg.norm(rij)
            if dist < 1e-5:
                continue
            direction = rij / dist
            # Attractive: weak force pulling together (Z<1)
            if regime == "attractive":
                f = 0.08 * np.exp(-dist + 1.2)
            # Repulsive: strong force pushing apart (Z>1)
            elif regime == "repulsive":
                f = -0.15 / (dist**2)
            else:
                f = 0
            forces[i] += f * direction
    return forces

# --- Plot setup ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
title = ax.set_title("", color='white', fontsize=16, pad=15)

# Scatter plot for particles
sc = ax.scatter(positions[:, 0], positions[:, 1], s=120, c='lime', edgecolors='black', alpha=0.9, zorder=10)
# Quiver for force arrows
quiver = ax.quiver(positions[:, 0], positions[:, 1], np.zeros(N), np.zeros(N), color='orange', scale=10, width=0.015, zorder=20)

def update(frame):
    global positions, interaction
    # Alternate between attractive and repulsive every 100 frames
    if frame % 200 < 100:
        regime = "attractive"
        title.set_text("Attractive regime (Z < 1): Particles cluster")
    else:
        regime = "repulsive"
        title.set_text("Repulsive regime (Z > 1): Particles spread out")
    # Compute forces
    forces = compute_forces(positions, regime)
    # Update positions (simple Euler integration)
    positions[:] += forces * 0.15
    # Keep particles inside the box
    positions[:] = np.clip(positions, r, L - r)
    # Update scatter and quiver
    sc.set_offsets(positions)
    quiver.set_offsets(positions)
    quiver.set_UVC(forces[:, 0], forces[:, 1])
    return sc, quiver, title

ani = FuncAnimation(fig, update, frames=400, interval=40, blit=False)
plt.tight_layout()
plt.show()

# --- Scientific background ---
# In real gases, the compressibility factor Z indicates the effect of intermolecular forces:
#   - Z < 1: Attractive forces dominate, causing particles to cluster (as in condensation).
#   - Z > 1: Repulsive forces dominate, causing particles to spread out (as in high-pressure gases).
# This animation visualizes these effects: particles cluster together when attraction dominates, and spread apart when repulsion dominates.
# The orange arrows show the direction and relative strength of the forces acting on each particle.