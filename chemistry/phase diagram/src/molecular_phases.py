import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Parameters ---
N = 40         # Number of molecules
L = 8          # Box size
r = 0.25       # Molecule radius

# --- Helper: solid lattice positions ---
def solid_positions(N, L):
    n_side = int(np.ceil(N ** (1/3)))
    grid = np.linspace(r, L - r, n_side)   
    X, Y, Z = np.meshgrid(grid, grid, grid)
    pos = np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T[:N]
    return pos

# --- Helper: random positions for liquid/gas ---
def random_positions(N, L, min_dist):
    positions = []
    while len(positions) < N:
        candidate = np.random.rand(3) * (L - 2*r) + r
        if all(np.linalg.norm(candidate - p) > min_dist for p in positions):
            positions.append(candidate)
    return np.array(positions)

# --- Animation states ---
states = [
    {"name": "Solid",   "min_dist": 1.0, "jitter": 0.08, "color": "#33aaff"},
    {"name": "Liquid",  "min_dist": 0.5, "jitter": 0.25, "color": "#33ffaa"},
    {"name": "Gas",     "min_dist": 0.1, "jitter": 1.0,  "color": "#ffaa33"},
]

frames_per_state = 60
total_frames = frames_per_state * (len(states) - 1)

# --- Figure setup ---
plt.style.use('dark_background')
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_zlim(0, L)
ax.set_box_aspect([1, 1, 1])
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
title = ax.set_title("", color='white', fontsize=18, pad=18)

# --- Initial positions ---
solid_pos = solid_positions(N, L)
liquid_pos = random_positions(N, L, states[1]["min_dist"])
gas_pos = random_positions(N, L, states[2]["min_dist"])

# --- Scatter plot for molecules ---
sc = ax.scatter([], [], [], s=120, c=[], edgecolors='black', alpha=0.85)

def get_state(frame):
    idx = frame // frames_per_state
    frac = (frame % frames_per_state) / frames_per_state
    if idx >= len(states) - 1:
        return states[-2], states[-1], 1.0
    return states[idx], states[idx+1], frac

# --- Animation update function ---
def update(frame):
    state_from, state_to, frac = get_state(frame)
    # Choose start/end positions
    if state_from["name"] == "Solid":
        pos_from = solid_pos + np.random.randn(N, 3) * state_from["jitter"]
    elif state_from["name"] == "Liquid":
        pos_from = liquid_pos + np.random.randn(N, 3) * state_from["jitter"]
    else:
        pos_from = gas_pos + np.random.randn(N, 3) * state_from["jitter"]

    if state_to["name"] == "Solid":
        pos_to = solid_pos + np.random.randn(N, 3) * state_to["jitter"]
    elif state_to["name"] == "Liquid":
        pos_to = liquid_pos + np.random.randn(N, 3) * state_to["jitter"]
    else:
        pos_to = gas_pos + np.random.randn(N, 3) * state_to["jitter"]

    # Interpolate positions
    positions = (1 - frac) * pos_from + frac * pos_to
    color = state_from["color"] if frac < 0.5 else state_to["color"]
    sc._offsets3d = (positions[:, 0], positions[:, 1], positions[:, 2])
    sc.set_facecolor(color)
    sc.set_edgecolor('black')
    title.set_text(f"{state_from['name']} → {state_to['name']}" if frac < 0.99 else f"{state_to['name']}")
    return sc, title

ani = FuncAnimation(fig, update, frames=total_frames, interval=80, blit=False)
plt.tight_layout()
plt.show()

# --- Scientific background ---
# This animation visualizes the behavior of molecules in different phases:
# - In the solid phase, molecules are arranged in a regular lattice and vibrate around fixed positions.
# - In the liquid phase, molecules are close together but move more freely, sliding past each other.
# - In the gas phase, molecules are far apart and move independently throughout the container.
# The transitions show melting (solid→liquid) and evaporation (liquid→gas), illustrating how molecular arrangement and motion change with phase.