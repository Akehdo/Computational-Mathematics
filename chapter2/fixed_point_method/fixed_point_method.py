import numpy as np
import math

def fixed_point(g, x0, e=1e-4, Nmax=100):
    n = 0
    x = x0

    while n < Nmax:
        x_next = g(x)

        # stop condition
        if abs(x_next -x) < e:
            return x_next

        x = x_next
        n += 1
    raise RuntimeError("failed to converge")


def g(x):
    return -(1/3) * x * math.log(x)

root = fixed_point(g, x0=0.1)
print("Approximate root:", root)