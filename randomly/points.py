import numpy as np
from scipy.stats import poisson, uniform
from typing import Tuple

def generate_poisson_points(bounds: Tuple[float, float, float, float], rate: float) -> np.ndarray:
    """Create cordinate pairs from a Poisson process

    Parameters
    ----------
    bounds : Tuple[float, float, float, float]
        ``(minx, miny, maxx, maxy)`` of the bounding box
    rate : float
        Theoretical events per unit area across the whole space.

    Returns
    -------
    np.ndarray
        Array of shape ``(N pairs, 2)`` where each pair is x and y coordinates
    inside the bounding box.
    """

    # Get sizes of sides of the area of interest
    dx = bounds[2] - bounds[0]
    dy = bounds[3] - bounds[1]

    N = poisson(rate * dx * dy).rvs()
    xs = uniform.rvs(0, dx, ((N, 1))) + bounds[0]
    ys = uniform.rvs(0, dy, ((N, 1))) + bounds[1]

    return np.hstack((xs, ys))
