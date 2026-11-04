def solve_maze(maze):
    """
    使用 DFS 解決老鼠走迷宮問題
    :param maze: 2D List (0 代表可行走，1 代表障礙物)
    :return: 標記路徑後的迷宮 (2 代表老鼠走過的路徑)，若無解則回傳 None
    """
    rows = len(maze)
    cols = len(maze[0])
    
    # 建立走訪記錄/路徑圖 (預設全為 0)
    solution = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def is_safe(r, c):
        # 檢查座標是否在界內、可通行且未被記錄在當前路徑中
        return 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and solution[r][c] == 0

    def dfs(r, c):
        # 終止條件：抵達終點
        if r == rows - 1 and c == cols - 1:
            solution[r][c] = 2
            return True
        
        if is_safe(r, c):
            # 標記當前節點為路徑之一
            solution[r][c] = 2
            
            # 定義探索方向：下、右、上、左
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                if dfs(r + dr, c + dc):
                    return True
            
            # 若四個方向皆無法通往出口，回溯 (Backtrack)
            solution[r][c] = 0
            return False
            
        return False

    # 起點為 (0, 0)
    if maze[0][0] == 0 and dfs(0, 0):
        return solution
    else:
        return None

# --- 測試範例 ---
if __name__ == "__main__":
    # 0: 路, 1: 牆
    maze_map = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]

    path = solve_maze(maze_map)
    if path:
        print("找到路徑 (2 表示走過的路徑):")
        for row in path:
            print(" ".join(str(cell) for cell in row))
    else:
        print("此迷宮無解。")
