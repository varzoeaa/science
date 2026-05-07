import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# parameters
L = 8           # box size
r = 0.3         # molecule radius
v = 4.0         # molecule speed (faster)
dt = 0.05       # time step
total_time = 20 # simulation time (seconds)
frames = int(total_time / dt)
wall_hits = 0   # collision counter

# initial
pos = np.array([L/2, L/2, L/2])
direction = np.random.randn(3)
direction /= np.linalg.norm(direction)
vel = direction * v
t = 0

# plot setup
plt.style.use('dark_background')
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_zlim(0, L)
ax.set_box_aspect([1, 1, 1])
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# draw box
def draw_box(ax, L, color='#888', lw=2, alpha=1.0):
    for s, e in [
        ([0, 0, 0], [L, 0, 0]), ([L, 0, 0], [L, L, 0]), ([L, L, 0], [0, L, 0]), ([0, L, 0], [0, 0, 0]),
        ([0, 0, L], [L, 0, L]), ([L, 0, L], [L, L, L]), ([L, L, L], [0, L, L]), ([0, L, L], [0, 0, L]),
        ([0, 0, 0], [0, 0, L]), ([L, 0, 0], [L, 0, L]), ([L, L, 0], [L, L, L]), ([0, L, 0], [0, L, L])
    ]:
        ax.plot3D(*zip(s, e), color=color, lw=lw, alpha=alpha)
draw_box(ax, L)

# particle setup
particle, = ax.plot([], [], [], 'o', color='lime', markersize=18, markeredgecolor='black', alpha=0.9)

# wall hit counter
counter_text = ax.text2D(0.05, 0.92, '', transform=ax.transAxes, fontsize=16, color='cyan', fontweight='bold')
pressure_text = ax.text2D(0.05, 0.86, '', transform=ax.transAxes, fontsize=16, color='orange', fontweight='bold')
formula_text = ax.text2D(0.5, 1.02, r"$p = \frac{F}{A} = \frac{\Delta p}{\Delta t \cdot A}$",
                         transform=ax.transAxes, fontsize=18, color='white', ha='center')

# update function for animation
hits = []
times = []

def update(frame):
    global pos, vel, t, wall_hits
    t += dt
    pos = pos + vel * dt

    hit = False
    for i in range(3):  # x, y, z
        if pos[i] < r:
            pos[i] = r
            vel[i] *= -1
            wall_hits += 1
            hit = True
        elif pos[i] > L - r:
            pos[i] = L - r
            vel[i] *= -1
            wall_hits += 1
            hit = True

    # for calculating pressure
    if hit:
        hits.append(1)
        times.append(t)
    else:
        hits.append(0)
        times.append(t)

    # momentum change and pressure calculation
    m = 1
    area = 1
    elapsed = t if t > 0 else 1
    delta_p = 2 * m * v * wall_hits
    pressure = delta_p / (elapsed * area)

    # visuals
    particle.set_data([pos[0]], [pos[1]])
    particle.set_3d_properties([pos[2]])
    counter_text.set_text(f"Wall collisions: {wall_hits}")
    pressure_text.set_text(f"Pressure: {pressure:.2f} (arb. units)")

    return particle, counter_text, pressure_text, formula_text

ani = FuncAnimation(fig, update, frames=frames, interval=dt*1000, blit=True)
plt.show()


# --- Scientific background ---
# This animation demonstrates the microscopic origin of gas pressure in a 3D box.
# A single particle moves inside the box, bouncing off the walls.
# Each time the particle collides with a wall, it transfers momentum to that wall.
# The pressure (p) exerted by the gas is defined as the force per unit area, and on the microscopic level,
#   it is related to the rate of momentum transfer from particle collisions:
#       p = F / A = Δp / (Δt ⋅ A)
# where Δp is the total momentum change delivered to the wall in time Δt, and A is the wall area.
# In this simulation, the number of wall collisions and the estimated pressure are tracked and displayed in real time.
# This model illustrates how the macroscopic property of pressure arises from the collective effect of many microscopic collisions,
#   as described by the kinetic theory of gases.