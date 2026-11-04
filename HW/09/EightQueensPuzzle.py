def solve_n_queens(n=8):
    solutions = []
    # 記錄每一行皇后的 column 索引：queens[row] = col
    queens = [-1] * n
    
    # 剪枝集合
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def dfs(row):
        # 終止條件：已成功放置 n 個皇后
        if row == n:
            solutions.append(list(queens))
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  # 衝突，剪枝

            # 做選擇
            queens[row] = col
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            # 遞迴深入下一行
            dfs(row + 1)

            # 回溯：復原狀態
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    dfs(0)
    return solutions

# 執行並印出結果概況
solutions = solve_n_queens(8)
print(f"8 皇后共有 {len(solutions)} 組解。")

# 視覺化第一組解
def print_board(solution):
    n = len(solution)
    for r in range(n):
        line = ["Q" if solution[r] == c else "." for c in range(n)]
        print(" ".join(line))

print("\n第一組解棋盤：")
print_board(solutions[0])
