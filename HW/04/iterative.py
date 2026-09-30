def fixed_point_multiple_root(x0, tolerance=1e-5, max_iterations=100):
    x = x0
    print(f"初始值 x0 = {x}\n")
    
    for i in range(max_iterations):
        next_x = (x**2 + 1.0) / 2.0
        
        print(f"第 {i+1} 次迭代: x = {next_x:.6f}")
        
        if abs(next_x - x) < tolerance:
            return next_x, i + 1
            
        x = next_x
        
    raise ValueError("超過最大迭代次數仍未收斂")

root, iterations = fixed_point_multiple_root(0.5)

print(f"\n不動點迭代求得的根為: {root:.6f}")
print(f"總共迭代次數: {iterations}")
