import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#time and wave
t = np.linspace(0,2 * np.pi, 200)
omega = 10

#3d 
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(0.2 * np.pi)
ax.set_facecolor("black")
ax.tick_params(colors ="white")

#background
ax.xaxis.set_pane_color((0,0,0,1))
ax.yaxis.set_pane_color((0,0,0,1))
ax.zaxis.set_pane_color((0,0,0,1))

#grid color
ax.xaxis._axinfo['grid'].update(color='white', linewidth=0.5)
ax.yaxis._axinfo['grid'].update(color='white', linewidth=0.5)
ax.zaxis._axinfo['grid'].update(color='white', linewidth=0.5)

#light wave
line, = ax.plot([], [], [], lw=2, color='cyan')

#meshgrid 
X_plane, Z_plane = np.meshgrid(np.linspace(-1.5, 1.5, 2), np.linspace(0, 2 * np.pi, 2))
Y_plane = np.zeros_like(X_plane)

#initial
plane = [ax.plot_surface(X_plane, Y_plane, Z_plane, color='white', alpha=0.0)]

def update(frame):
    if plane:
        plane[0].remove()
    z = t[:frame]

    if frame < 100:
        x = np.sin(omega * z)
        y = np.sin(omega * z + np.pi / 3)
        alpha = 0.05
    else:
        x = np.sin(omega * z)
        y = np.zeros_like(z)
        alpha=0.2

    plane[0] = ax.plot_surface(X_plane, Y_plane, Z_plane, color='white', alpha = alpha)

    line.set_data(x,y)
    line.set_3d_properties(z)
    return line, plane[0]

ani = FuncAnimation(fig, update, frames=len(t), interval=40, blit=False)
plt.show()
