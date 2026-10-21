def nCr_dp(n: int, k: int) -> int:
    # 邊界與對稱性質優化
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)

    # dp[j] 表示當前列的 C(i, j)
    dp = [0] * (k + 1)
    dp[0] = 1  # C(i, 0) 恆為 1

    for i in range(1, n + 1):
        # 逆序更新，確保使用的是 i-1 列的舊值
        for j in range(min(i, k), 0, -1):
            dp[j] = dp[j] + dp[j - 1]

    return dp[k]
