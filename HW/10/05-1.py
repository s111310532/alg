import itertools

def f(x):
    return sum(xi**2 for xi in x)

def integral(f, low, high, max_evals=100000):
    n = len(low)
    steps = max(1, int(max_evals ** (1.0 / n)))
    
    grids = []
    cell_volume = 1.0
    for a, b in zip(low, high):
        dx = (b - a) / steps
        cell_volume *= dx
        grids.append([a + (i + 0.5) * dx for i in range(steps)])
        
    total = 0.0
    for point in itertools.product(*grids):
        total += f(point)
        
    return total * cell_volume

print("=== 1. 黎曼積分法 (Riemann Sum) ===")
for dim in [1, 2, 5, 100]:
    low = [0.0] * dim
    high = [1.0] * dim
    ans = integral(f, low, high)
    exact = dim / 3.0
    print(f"{dim:>3} 維 | 黎曼積分: {ans:.6f} | 理論值 (n/3): {exact:.6f}")
