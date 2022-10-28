# Mandelbrot-Julia Project

*By Paul TRINCKLIN and Alexis DELAGE*

## Installation

```bash
pip install .
```


## Documentation

### Website

![https://hydrielax.github.io/mandelbrot-papy/](https://hydrielax.github.io/mandelbrot-papy/)

### Mandelbrot

Create a Mandelbrot figure.

#### Usage

```
mandelbrotPlot [-h] [--zmin ZMIN] [--zmax ZMAX] [--pixel-size PIXEL_SIZE] [--max-iter MAX_ITER] [--output FIGNAME]
```

#### Options

* `--zmin ZMIN`: The minimum complex number (down-left corner)
* `--zmax ZMAX`: The maximum complex number (up-right corner)
* `--pixel-size PIXEL_SIZE, -s PIXEL_SIZE`: The size of a pixel in the complex plane
* `--max-iter MAX_ITER, -i MAX_ITER`: The maximum number of iterations
* `--output FIGNAME, -o FIGNAME`: The name of the file where the picture will be saved.

### Julia

Create a Julia figure.

#### Usage 

```
juliaPlot [-h] [--candidate C] [--zmin ZMIN] [--zmax ZMAX] [--pixel-size PIXEL_SIZE] [--max-iter MAX_ITER] [--output FIGNAME]
```

#### Options

* `--candidate C, -c C`: Parameter defining a specific Julia set
* `--zmin ZMIN`: The minimum complex number (down-left corner)
* `--zmax ZMAX`: The maximum complex number (up-right corner)
* `--pixel-size PIXEL_SIZE, -s PIXEL_SIZE`: The size of a pixel in the complex plane
* `--max-iter MAX_ITER, -i MAX_ITER`: The maximum number of iterations
* `--output FIGNAME, -o FIGNAME`: The name of the file where the picture will be saved.
