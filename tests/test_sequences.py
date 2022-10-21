from mandelbrot.is_in_set import is_in_mandelbrot, is_in_julia
from random import random


def test_mandelbrot():
    assert is_in_mandelbrot(0.251, 50) == True
    assert is_in_mandelbrot(0.251, 100) == False
    assert is_in_mandelbrot(1) == False


def test_julia():
    assert is_in_julia(0.25+0.25j, 0.25)


def test_julia_mandelbrot():
    for _ in range(100):
        c = (4*random()-2) + (2*random()-1)*1j
        assert is_in_julia(0, c) == is_in_mandelbrot(c)
