import numpy as np

def gauss(x, sigma=1.0):
    t = -0.5 * x**2 / sigma**2
    return np.exp(t)

def normal_samples(N, sigma):
    return np.random.randn(N) * sigma
    