import math
import random

# 範例城市座標 (x, y)
cities = [
    (0, 0), (1, 5), (5, 2), (6, 6), (8, 3),
    (2, 7), (4, 9), (9, 8), (7, 1), (3, 3)
]
num_cities = len(cities)

# 建立對稱距離矩陣
dist_matrix = [
    [math.hypot(c1[0] - c2[0], c1[1] - c2[1]) for c2 in cities]
    for c1 in cities
]

def path_length(path):
    """計算封閉路徑總長度（回到起點）"""
    total = 0
    n = len(path)
    for i in range(n):
        u = path[i]
        v = path[(i + 1) % n]
        total += dist_matrix[u][v]
    return total
