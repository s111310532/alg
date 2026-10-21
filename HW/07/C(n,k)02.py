def nCr_non_dp(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

    # 利用對稱性減少迭代次數
    k = min(k, n - k)
    result = 1

    for i in range(1, k + 1):
        # 先乘後除，保證每次除以 i 時必能整除
        result = result * (n - k + i) // i

    return result
