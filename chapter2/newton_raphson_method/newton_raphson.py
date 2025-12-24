def newton_raphson(f, df, x0, eps=1e-6, Nmax=100):
    x = x0

    for n in range(Nmax):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ValueError("Derivative is zero")

        x_next = x - fx / dfx
        print(f"n={n}, x={x}, x_next={x_next}")

        if abs(x_next - x) < eps:
            return x_next

        x = x_next

    raise RuntimeError("failed to converge")

def f(x):
    return x**3 - 2*x - 5

def df(x):
    return 3*x**2 - 2

root = newton_raphson(f, df, 2)
print("Approximate root:", root)