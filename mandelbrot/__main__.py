import argparse
from img_generator import plot_mandelbrot, plot_julia

def mandelbrot():
    parser = argparse.ArgumentParser(description='Create a mandelbrot figure.')
    parser.add_argument(
        '--zmin',
        default= -2 - 1.5j,
        type=complex,
        help="The minimum complex number (down-left corner)"
    )
    parser.add_argument(
        '--zmax',
        default= 1 + 1.5j,
        type=complex,
        help="The maximum complex number (up-right corner)"
    )
    parser.add_argument(
        '--pixel-size', '-s',
        default=5e-3,
        type=float,
        help="The size of a pixel in the complex plane"
    )
    parser.add_argument(
        '--max-iter', '-i',
        default=200,
        type=int,
        help="The maximum number of iterations"
    )
    parser.add_argument(
        '--output', '-o',
        dest='figname',
        default='Mandelbrot figure.png',
        type=str,
        help="The name of the file where the picture will be saved."
    )
    args = parser.parse_args()
    plot_mandelbrot(**args)