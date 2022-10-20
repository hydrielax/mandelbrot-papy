

def seq(z: complex, c: complex) -> complex:
    """Generate the next element for the $z_{n+1}=z_n^2+c$ sequence.

    Parameters
    ----------
    z : complex
        The 0-th element of the sequence
    c : complex
        The candidate number to test

    Returns
    -------
    complex
        The n-th element of the sequence.

    Yields
    ------
    Iterator[complex]
        The sequence for this candidate number
    """

    while True:
        yield z
        z = z ** 2 + c


def is_in_mandelbrot(candidate: complex, itermax: int = 200) -> bool:
    """Test if a candidate complex number is within the Mandelbrot space.

    Parameters
    ----------
    candidate : complex
        The candidate complex number.
    itermax : int, optional
        The maximum number of iteration, by default 200

    Returns
    -------
    bool
        True if the candidate number is within the Mandelbrot space, else False.
    """
    return is_in_julia(0, candidate, itermax)


def is_in_julia(z0: complex, candidate: complex, itermax: int = 200) -> bool:
    """Test if a candidate complex number is within the Julia space.

    Parameters
    ----------
    z0 : complex
        The first element of the sequence for Julia
    candidate : complex
        The candidate complex number.
    itermax : int, optional
        The maximum number of iteration, by default 200

    Returns
    -------
    bool
        True if the candidate number is within the Julia space, else False.
    """

    i = 0
    z = z0
    sequence = seq(z, candidate)
    while i < itermax and abs(z) <= 2:
        z = next(sequence)
        i += 1
    return abs(z) <= 2