import argparse
from .img_generator import plot_mandelbrot, plot_julia


def add_common_args(parser):
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


def mandelbrot():
    parser = argparse.ArgumentParser(description='Create a Mandelbrot figure.')
    add_common_args(parser)
    kwargs = dict(parser.parse_args()._get_kwargs())
    plot_mandelbrot(**kwargs)


def julia():
    parser = argparse.ArgumentParser(description='Create a Julia figure.')
    parser.add_argument(
        '--candidate', '-c',
        dest='c',
        default= -0.8 + 0.156j,
        type=complex,
        help="Parameter defining a specific Julia set"
    )
    add_common_args(parser)
    kwargs = dict(parser.parse_args()._get_kwargs())
    plot_julia(**kwargs)
