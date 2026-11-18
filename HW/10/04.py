def mc_integral_nd(f, low, high, samples=200000):
    n = len(low)
    volume = 1.0
    for i in range(n):
        volume *= (high[i] - low[i])
        
    total = 0.0
    for _ in range(samples):
        point = [random.uniform(low[i], high[i]) for i in range(n)]
        total += f(point)
        
    return volume * (total / samples)

print(f"4. 3維蒙地卡羅積分: {mc_integral_nd(f_3d, [0, 0, 0], [1, 1, 1]):.6f}")
