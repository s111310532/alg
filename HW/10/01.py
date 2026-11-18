import math

def diff_1d(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

def integral_1d(f, a, b, n=100000):
    dx = (b - a) / n
    total = 0.0
    for i in range(n):
        x = a + (i + 0.5) * dx
        total += f(x) * dx
    return total

f = lambda x: x**2
print(f"1. x=2 的微分值: {diff_1d(f, 2):.6f} (理論值: 4)")
print(f"   [0, 3] 積分值: {integral_1d(f, 0, 3):.6f} (理論值: 9)")
