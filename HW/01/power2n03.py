memo = {}
def power2n_3(n):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = power2n_3(n - 1) + power2n_3(n - 1)
    return memo[n]

def test(func, n, name):
    if func == power2n_2a and n > 30:
        print(f"[{name}] n = {n}: 無法完成（時間過長，直接跳過）")
        return

    start = time.perf_counter()
    try:
        result = func(n)
        end = time.perf_counter()
        print(f"[{name}] n = {n}: 耗時 {end - start:.8f} 秒")
    except RecursionError:
        print(f"[{name}] n = {n}: 遞迴深度超出上限 (RecursionError)")

