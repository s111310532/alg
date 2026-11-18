def gradient(f, x, h=1e-6):
    grad = []
    for i in range(len(x)):
        x_plus = list(x)
        x_minus = list(x)
        x_plus[i] += h
        x_minus[i] -= h
        grad.append((f(x_plus) - f(x_minus)) / (2 * h))
    return grad

def integral_nd_riemann(f, low, high, steps_per_dim=20):
    n = len(low)
    
    def recurse(dim, current_x):
        if dim == n:
            return f(current_x)
        a, b = low[dim], high[dim]
        dx = (b - a) / steps_per_dim
        total = 0.0
        for i in range(steps_per_dim):
            val = a + (i + 0.5) * dx
            total += recurse(dim + 1, current_x + [val]) * dx
        return total

    return recurse(0, [])

f_3d = lambda p: sum(p)
print(f"3. [1, 2, 3] 的梯度: {[round(g, 6) for g in gradient(f_3d, [1, 2, 3])]}")
print(f"   3維黎曼積分: {integral_nd_riemann(f_3d, [0, 0, 0], [1, 1, 1]):.6f}")
