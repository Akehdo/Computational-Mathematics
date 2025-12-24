import cmath

def muller(f, x0, x1, x2, eps=1e-6, Nmax=100):
    n = 0

    while n < Nmax:
        y0 = f(x0)
        y1 = f(x1)
        y2 = f(x2)

        h0 = x1 - x0
        h1 = x2 - x1

        d0 = (y1 - y0) / h0
        d1 = (y2 - y1) / h1

        a = (d1 - d0) / (h1 + h0)
        b = a * h1 + d1
        c = y2

        D = cmath.sqrt(b*b - 4*a*c)

        # choose sign to maximize denominator magnitude
        if abs(b + D) > abs(b - D):
            denom = b + D
        else:
            denom = b - D

        if denom == 0:
            raise ValueError("Zero denominator in Muller method")

        x_new = x2 - (2 * c) / denom

        # stopping condition
        if abs(f(x_new)) < eps:
            return x_new

        # shift points
        x0, x1, x2 = x1, x2, x_new
        n += 1

    raise RuntimeError("Method failed after Nmax iterations")


def f(x):
    return cmath.cos(x) - x * cmath.exp(x)

root = muller(f, -1, 0, 1)
print("Approximate root:", root)
