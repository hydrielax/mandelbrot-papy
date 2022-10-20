import argparse
from .img_generator import plot_mandelbrot, plot_julia


def add_common_args(parser):
    """Add the arguments to the parser that are commons to both Mandelbrot and
    Julia figures.

    Parameters
    ----------
    parser : _type_
        The parser to which we want to add the arguments.
    """

    parser.add_argument(
        '--zmin',
        type=complex,
        help="The minimum complex number (down-left corner)"
    )
    parser.add_argument(
        '--zmax',
        type=complex,
        help="The maximum complex number (up-right corner)"
    )
    parser.add_argument(
        '--pixel-size', '-s',
        type=float,
        help="The size of a pixel in the complex plane"
    )
    parser.add_argument(
        '--max-iter', '-i',
        type=int,
        help="The maximum number of iterations"
    )
    parser.add_argument(
        '--output', '-o',
        dest='figname',
        type=str,
        help="The name of the file where the picture will be saved."
    )


def mandelbrot():
    """Main Mandelbrot command for CLI."""
    parser = argparse.ArgumentParser(description='Create a Mandelbrot figure.')
    add_common_args(parser)
    kwargs = {kw: arg for (kw, arg) in parser.parse_args()._get_kwargs() if arg is not None}
    plot_mandelbrot(**kwargs)


def julia():
    """Main Julia command for CLI."""
    parser = argparse.ArgumentParser(description='Create a Julia figure.')
    parser.add_argument(
        '--candidate', '-c',
        dest='c',
        type=complex,
        help="Parameter defining a specific Julia set"
    )
    add_common_args(parser)
    kwargs = {kw: arg for (kw, arg) in parser.parse_args()._get_kwargs() if arg is not None}
    plot_julia(**kwargs)
