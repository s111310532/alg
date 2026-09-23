計算 $2^n$ 的演算法效能分析

1.方法 1：使用 Python 內建的次方運算子 2**n。底層使用  C 語言實現快速冪（Binary Exponentiation）。
2.方法 2a (power2n_2a)：使用對稱雙遞迴 power2n(n-1) + power2n(n-1)，無快取機制。
3.方法 2b (power2n_2b)：使用線性單遞迴 2 * power2n(n-1)。
4.方法 3 (power2n_3)：使用雙遞迴搭配字典查表（Memoization / 記憶化）。

Q: 哪一個最快？
A:方法 1 最快。Python 的 ** 運算子在底層是利用快速冪演算法實現，計算 $n = 100$ 只需要約 $\log_2(100) \approx 7$ 次乘法，且在 C 語言層級執行，沒有 Python 函式呼叫堆疊的開銷。
 

