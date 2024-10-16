import numpy as np
import matplotlib.pyplot as plt

def metrolplis(x: int, dist: tuple) -> int:
    n = len(dist)
    # Propose
    p = np.random.rand()
    if p < 0.1:
        proposed = x + 1
    else:
        proposed = x - 1
    # Wrapback
    proposed %= n

    # Accept?
    p = np.random.rand()
    p1 = dist[x]
    p2 = dist[proposed]

    if p < p2 / p1:
        return proposed
    else:
        return x

dist = (0.2, 0.5, 0.3)
samples = []
x0 = 0
x = x0
for i in range(10000):
    samples.append(x)
    x = metrolplis(x, dist)

a = samples.count(0)
b = samples.count(1)
c = samples.count(2)
print(a, b, c)