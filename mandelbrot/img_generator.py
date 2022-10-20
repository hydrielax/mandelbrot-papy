import numpy as np
from PIL import Image

from .is_in_set import is_in_mandelbrot, is_in_julia

def plot_mandelbrot(
    zmin: complex = -2 - 1.5j,
    zmax: complex = 1 + 1.5j,
    pixel_size: float = 5e-3,
    max_iter: int = 200,
    figname: str = 'Mandelbrot figure.png'
) -> None:
    """Create a Mandelbrot figure with the given parameters.

    Parameters
    ----------
    zmin : complex
        The minimum complex number (down-left corner)
    zmax : complex
        The maximum complex number (up-right corner)
    pixel_size : float
        The size of a pixel in the complex pl
    max_iter : int
        The maximum number of iterations
    figname : str
        The name of the file where the picture will be saved.
    """

    x = np.arange(zmin.real, zmax.real, pixel_size)
    y = - np.arange(zmin.imag, zmax.imag, pixel_size)
    xx, yy = np.meshgrid(x, y)
    grid = xx + yy*1j
    vec_is_in_mandelbrot = np.vectorize(is_in_mandelbrot)
    mandelbrot_set = vec_is_in_mandelbrot(grid, max_iter)
    pil_image = Image.fromarray(np.invert(mandelbrot_set))
    pil_image.save(figname)


def plot_julia(
    c: complex = -0.8 + 0.156j,
    zmin: complex = -2 - 1j,
    zmax: complex = 2 + 1j,
    pixel_size: float = 5e-3,
    max_iter: int = 200,
    figname: str = 'Julia figure.png'
) -> None:
    """Create a Julia figure with the given parameters.

    Parameters
    ----------
    c: complex
        Parameter defining a specific Julia set
    zmin : complex
        The minimum complex number (down-left corner)
    zmax : complex
        The maximum complex number (up-right corner)
    pixel_size : int
        The size of the picture width in pixels
    max_iter : int
        The maximum number of iterations
    figname : str
        The name of the file where the picture will be saved.
    """

    x = np.arange(zmin.real, zmax.real, pixel_size)
    y = - np.arange(zmin.imag, zmax.imag, pixel_size)
    xx, yy = np.meshgrid(x, y)
    grid = xx + yy*1j
    vec_is_in_julia = np.vectorize(is_in_julia)
    julia_set = vec_is_in_julia(grid, c, max_iter)
    pil_image = Image.fromarray(np.invert(julia_set))
    pil_image.save(figname)
