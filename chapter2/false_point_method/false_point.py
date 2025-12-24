import math

def false_position(f, a, b, eps=1e-6, Nmax=100):
    fa = f(a)
    fb = f(b)

    # Check initial bracketing condition
    if fa * fb >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    for n in range(1, Nmax + 1):
        # False position formula
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x)

        print(f"n={n}, a={a}, b={b}, x={x}, f(x)={fx}")

        # stopping condition
        if abs(fx) < eps:
            return x

        # update interval
        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

    raise RuntimeError("Failed to converge after Nmax iterations")

def f(x):
    return 2 * math.exp(x) * math.sin(x) - 3

root = false_position(f, 0, 1)
print("Approximate root:", root)
