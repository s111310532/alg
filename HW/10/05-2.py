import random

def mc_integral(f, low, high, samples=200000):
    n = len(low)
    volume = 1.0
    for a, b in zip(low, high):
        volume *= (b - a)
        
    total = 0.0
    for _ in range(samples):
        point = [random.uniform(low[i], high[i]) for i in range(n)]
        total += f(point)
        
    return volume * (total / samples)

print("\n=== 2. 蒙地卡羅法 (Monte Carlo) ===")
for dim in [1, 2, 5, 100]:
    low = [0.0] * dim
    high = [1.0] * dim
    ans = mc_integral(f, low, high)
    exact = dim / 3.0
    print(f"{dim:>3} 維 | 蒙地卡羅: {ans:.6f} | 理論值 (n/3): {exact:.6f}")
