import random

def mc_integral_1d(f, a, b, samples=100000):
    total = 0.0
    for _ in range(samples):
        x = random.uniform(a, b)
        total += f(x)
    return (b - a) * (total / samples)

print(f"2. 單變數蒙地卡羅積分 (x^2 在 [0, 3]): {mc_integral_1d(f, 0, 3):.6f}")
