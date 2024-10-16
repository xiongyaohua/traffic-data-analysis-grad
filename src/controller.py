from world import World
from sensor_model import gauss, normal_samples
import numpy as np
from pygame import Vector2

# 假设偏向角完全准确
def likelihood_single(world: World, pos, alpha, dist_sample, sigma):
    dist_simulate = world.ray_trace(pos, alpha)
    e = dist_simulate - dist_sample
    pr = gauss(e, sigma)

    return pr

# 假设偏向角有误差
def likelihood_mutiple(world: World, pos, alpha, sigma_alpha, dist_sample, sigma):
    N = 10
    alpha_samples = normal_samples(N, sigma_alpha)
    prs = [likelihood_single(
        world, pos, alpha, dist_sample, sigma
    ) for alpha in alpha_samples]

    return np.array(prs).mean()

def likelihood(world, dist, alpha):
    SIGMA_ALPHA = 2.0
    SIGMA = 10.0
    N = 51
    xs = np.linspace(0, 1000, N)
    ys = np.linspace(0, 1000, N)

    P = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            x = xs[i]
            y = ys[i]
            pos = Vector2(x, y)
            P[i, j] = likelihood_mutiple(world, pos, alpha, SIGMA_ALPHA, dist, SIGMA)

    return P

def _float_seperate(f):
    i = int(f)
    f -= i
    return i, f

def predict(Pr, v):
    x, y = v
    xi, xf = _float_seperate(f)
    yi, yf = _float_seperate(f)

    # TODO Finish it

if __name__ == "__main__":
    import matplotlib
    #matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np


    world = World()
    world.add_wall((400, 300), (600, 300))

    Pr = likelihood(world, 180, 0.3)
    print(Pr)
    print(Pr.sum())
    plt.imshow(Pr)
    plt.savefig("aaa.png")
