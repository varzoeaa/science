import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    """
    Generates the Mandelbrot set for a given region of the complex plane.

    Parameters:
        width (int): number of pixels along the x-axis (horizontal resolution)
        height (int): number of pixels along the y-axis (vertical resolution)
        x_min (float): minimum value of the real axis
        x_max (float): maximum value of the real axis
        y_min (float): minimum value of the imaginary axis
        y_max (float): maximum value of the imaginary axis
        max_iter (int): maximum number of iterations to determine divergence

    Returns:
        div_time (ndarray): 2D array where each value represents the iteration
                            count at which the corresponding point diverged.
    """
    # create a grid of complex numbers
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)

    # create a meshgrid for complex plane
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y  # create complex numbers from the grid

    # initialize Z to zero --> Z is the iterative variable
    Z = np.zeros_like(C)
    # divergence time array to store the iteration counts 
    div_time = np.zeros(C.shape, dtype=int)

    # mask to track which points have not yet diverged
    mask = np.full(C.shape, True, dtype=bool)

    # mandelbrot iteration: z = z^2 + c
    # for each point in the complex plane, iterate until divergence or max_iter
    for i in range(max_iter):
        Z[mask] = Z[mask]**2 + C[mask]  # only update points that have not diverged
        mask_new = abs(Z) <= 2          #points that remain bounded
        div_time[mask & ~mask_new] = i  # record the iteration count for points that just diverged
        mask = mask_new                 # update the mask 

    # points that never diverged within max_iter will have div_time = 0
    return div_time

def create_zoom_animation(x_center, y_center, zoom_start, zoom_end, frames, width, height, max_iter):
    """
    Creates and displays an animated zoom into the Mandelbrot set.

    Parameters:
        x_center, y_center (float): center of the zoom in the complex plane
        zoom_start (float): initial zoom level (1.0 means no zoom)
        zoom_end (float): final zoom level
        frames (int): number of animation frames
        width, height (int): resolution of the generated images
        max_iter (int): maximum number of iterations for Mandelbrot calculation
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.axis("off")  # hide the axes

    # initial Mandelbrot image at no zoom
    mandelbrot_image = mandelbrot(width, height, -2, 1, -1.5, 1.5, max_iter)
    im = ax.imshow(mandelbrot_image, cmap="twilight_shifted", animated=True)

    def update(frame):
        # calculate the zoom level and the corresponding window in the complex plane
        zoom = zoom_start * ((zoom_end / zoom_start) ** (frame / (frames - 1)))
        x_range = 3.0 / zoom
        y_range = 3.0 / zoom
        x_min = x_center - x_range / 2
        x_max = x_center + x_range / 2
        y_min = y_center - y_range / 2
        y_max = y_center + y_range / 2

        # generate the Mandelbrot set for the current zoom level
        mandelbrot_image = mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)
        im.set_data(mandelbrot_image)
        im.set_extent((x_min, x_max, y_min, y_max))
        ax.set_title(f"Zoom: {zoom:.2f}x")
        return [im]

    ani = animation.FuncAnimation(fig, update, frames=frames, blit=True, repeat=False)
    plt.show()

# --- Scientific background ---
# The Mandelbrot set is a fractal in the complex plane, defined by iterating z_{n+1} = z_n^2 + c from z_0 = 0.
# Points c for which the sequence remains bounded (|z| <= 2) after many iterations are in the Mandelbrot set.
# This animation zooms into a chosen region, revealing the fractal's self-similar, infinitely complex boundary.

# parameters for the zoom animation
x_center = -1.05   # real part of zoom center
y_center = 0.25    # imaginary part of zoom center
zoom_start = 1.0   # initial zoom (no zoom)
zoom_end = 50000.0 # final zoom (very deep)
frames = 30        # number of frames in the animation
width, height = 800, 800  # image resolution
max_iter = 200     # iteration limit for Mandelbrot calculation

create_zoom_animation(x_center, y_center, zoom_start, zoom_end, frames, width, height, max_iter)