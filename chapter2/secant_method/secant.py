def secant(f, x0, x1, eps=1e-6, Nmax=100):
    n=1

    f0 = f(x0)
    f1 = f(x1)

    while n <= Nmax:
        if f1 - f0 == 0:
            raise ValueError("Division by zero in secant method")

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = f(x2)

        print(f"n={n}, x0={x0}, x1={x1}, x2={x2}")

        # stopping condition
        if abs(f2) < eps:
            return x2

        # update for next iteration
        x0, f0 = x1, f1
        x1, f1 = x2, f2
        n += 1


    raise RuntimeError("Failed to converge after Nmax iterations")

def f(x):
    return x**3 - 2*x - 5

root = secant(f, x0=2, x1=3)
print("Approximate root:", root)
