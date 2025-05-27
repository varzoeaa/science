import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# time and wave parameters
t = np.linspace(0, 2 * np.pi, 200)  
omega = 10 # angular frequency

# 3d plotting setup
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(0, 2 * np.pi)
ax.set_facecolor("black")
ax.set_title("Polarized Light", color='white')
ax.tick_params(colors='white')

# background color for axes
ax.xaxis.set_pane_color((0,0,0,1))
ax.yaxis.set_pane_color((0,0,0,1))
ax.zaxis.set_pane_color((0,0,0,1))

# grid color
ax.xaxis._axinfo['grid'].update(color = 'white', linewidth=0.5)
ax.yaxis._axinfo['grid'].update(color = 'white', linewidth=0.5)
ax.zaxis._axinfo['grid'].update(color = 'white', linewidth=0.5)

# light wave line
line, = ax.plot([], [], [], lw=2, color="cyan")

# meshgrid for the polarizer plane
X_plane, Z_plane = np.meshgrid(np.linspace(-1.5, 1.5, 2), np.linspace(0, 2 * np.pi, 2))
Y_plane = np.zeros_like(X_plane)

# initially, the polarizer plane is not visible
plane = [ax.plot_surface(X_plane, Y_plane, Z_plane, color='white', alpha=0.0)]

def update(frame):
    """
    Animation update function.
    - For the first half of the animation, show an elliptically polarized wave.
    - After halfway, show the effect of a polarizer: only the x-component remains (linearly polarized).
    - The polarizer plane becomes more visible after the transition.
    """
    # remove the previous polarizer plane if it exists
    if plane:
        plane[0].remove()
    z = t[:frame]
    if frame < 100:
        # elliptically polarized light: both x and y components oscillate
        x = np.sin(omega * z)
        y = np.sin(omega * z + np.pi / 3)
        alpha = 0.05  
    else:
        # after the polarizer, only the x-component remains
        x = np.sin(omega * z)
        y = np.zeros_like(z)
        alpha = 0.2   

    # update the polarizer plane visibility
    plane[0] = ax.plot_surface(X_plane, Y_plane, Z_plane, color='white', alpha=alpha)

    # update the light wave line
    line.set_data(x, y)
    line.set_3d_properties(z)
    return line, plane[0]

#qanimation setup
ani = FuncAnimation(fig, update, frames=len(t), interval=40, blit=False)
plt.show()

# --- Scientific background ---
# This animation helps you see what happens to light as it passes through a polarizing filter.
# Light is an electromagnetic wave, and its electric field can wiggle in different directions.
# At first, the light in the animation is elliptically polarized: its electric field moves in both the x and y directions, tracing out an ellipse as it travels forward.
# Halfway through, a polarizer appears (the white plane at y=0). This filter only lets the x-direction through, blocking the y-direction.
# After passing through the polarizer, the light is linearly polarized: now the electric field only wiggles along the x-axis.
# This is a key idea in optics, and it’s used in everyday things like sunglasses, LCD screens, and cameras.