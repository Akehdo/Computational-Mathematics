import numpy as np

# you can add logs for values on every interation using print()
def bisection(f, a, b, eps=1e-4, Nmax=100):
    # Check initial condition
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) * f(b) must be < 0 ")

    n = 0
    fa = f(a)
    fb = f(b)

    while n <= Nmax:
        # midpoint
        c = (a + b) / 2

        fc = f(c)

        # stop condition
        if abs(fc) < eps or (b - a) / 2 < eps:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        n += 1

    raise RuntimeError("failed to converge")


# example of usage:
def f(x):
    return x ** 3 - x - 2


root = bisection(f, a=1, b=2, eps=0.01)
print("Approximate root:", root)
