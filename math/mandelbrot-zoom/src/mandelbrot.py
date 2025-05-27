import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    """
    Generates the Mandelbrot set for a given region of the complex plane.

    Parameters:
        width (int): Number of pixels along the x-axis (horizontal resolution).
        height (int): Number of pixels along the y-axis (vertical resolution).
        x_min (float): Minimum value of the real axis.
        x_max (float): Maximum value of the real axis.
        y_min (float): Minimum value of the imaginary axis.
        y_max (float): Maximum value of the imaginary axis.
        max_iter (int): Maximum number of iterations to determine divergence.

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

def plot_mandelbrot(div_time, x_min, x_max, y_min, y_max):
    """
    Plots the Mandelbrot set using matplotlib.

    Parameters:
        div_time (ndarray): 2D array of divergence iteration counts.
        x_min, x_max, y_min, y_max (float): Bounds of the plot in the complex plane.
    """
    plt.figure(figsize=(8, 8))
    # display the divergence time as an image
    plt.imshow(div_time, cmap="twilight_shifted", extent=(x_min, x_max, y_min, y_max))
    plt.title("Mandelbrot Set")
    plt.axis("off")  # hide the axes
    plt.tight_layout()
    plt.show()

# --- Scientific background ---
# The Mandelbrot set is a fascinating and iconic fractal that lives in the complex plane.
# To determine if a point c belongs to the Mandelbrot set, we start with z = 0 and repeatedly apply the rule z = z^2 + c.
# If this sequence stays bounded (meaning |z| never grows beyond 2, no matter how many times we iterate), then c is part of the Mandelbrot set.
# If the sequence escapes (|z| becomes greater than 2), c is not in the set.
# When visualizing, we color each point based on how quickly the sequence escapes—this reveals the intricate, infinitely detailed boundary of the Mandelbrot set.