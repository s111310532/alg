from collections import deque

def lee_maze_route(grid, start, target):
    """
    grid: 2D 二維矩陣
          0 = 空白可用金屬軌道
          -1 = 障礙物 (已存在導線或 Blockage)
    start: (row, col) 起點接腳
    target: (row, col) 目標接腳
    回傳: 最短走線座標清單 [(r0, c0), (r1, c1), ...]
    """
    rows, cols = len(grid), len(grid[0])
    sr, sc = start
    tr, tc = target

    if start == target:
        return [start]

    # wave_grid 紀錄擴展步數；-1 為未造訪
    wave_grid = [[-1] * cols for _ in range(rows)]
    
    # 標記既有障礙物不可走
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == -1:
                wave_grid[r][c] = -2  # 代表障礙

    # 4 方向移動：上下左右 (標準 Manhattan Routing)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 1. 波前擴展 (BFS)
    queue = deque([start])
    wave_grid[sr][sc] = 0
    found = False

    while queue:
        curr_r, curr_c = queue.popleft()
        curr_dist = wave_grid[curr_r][curr_c]

        if (curr_r, curr_c) == target:
            found = True
            break

        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                # 只有未造訪且非障礙物的格子才能擴展
                if wave_grid[nr][nc] == -1:
                    wave_grid[nr][nc] = curr_dist + 1
                    queue.append((nr, nc))

    if not found:
        return None  # 無法繞通 (Blocked)

    # 2. 回溯路徑 (Backtracing)
    path = [target]
    curr = target
    while curr != start:
        cr, cc = curr
        target_dist = wave_grid[cr][cc] - 1
        
        # 尋找鄰居中步數等於 target_dist 的格子
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if wave_grid[nr][nc] == target_dist:
                    path.append((nr, nc))
                    curr = (nr, nc)
                    break

    path.reverse()
    return path

# 測試範例
# 0: 空白, -1: 障礙物
chip_grid = [
    [ 0,  0,  0,  0,  0],
    [-1, -1, -1,  0,  0],
    [ 0,  0, -1,  0,  0],
    [ 0, -1, -1, -1,  0],
    [ 0,  0,  0,  0,  0]
]

pin_a = (0, 0)
pin_b = (4, 0)
wire = lee_maze_route(chip_grid, pin_a, pin_b)

print("繞線成功路徑：", wire)
