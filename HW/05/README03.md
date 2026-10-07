Bubble Sort

1.遞迴深度的安全設定

 將 PYTHON 遞迴上限設於 2000。

2.自製高階函式

 利用 Python 的 Slice 將串列拆成 seq[0]」與 seq[1]

 *my_map(fn, seq)：若串列為空返回 []；否則對 seq[0] 套用函式 fn，並與後續遞迴結果拼接。

 *my_filter(predicate, seq)：檢查 seq[0] 是否符合條件 predicate。符合就保留並接上遞迴結果，不符合就捨棄。

 *my_reduce(fn, acc, seq)：取出 seq[0]，呼叫 fn(acc, seq[0]) 更新累加器 acc，再將新的 acc 與剩下的 seq[1:] 丟入下一層遞迴，直到串列被清空為止。

3. 單趟冒泡：利用 my_reduce 取代內層迴圈

 累加器 acc 設計成一個 Tuple。

 若 current_max > val：表示前面的數較大，應該後移。因此把較小的 val 放進前綴串列，並繼續「帶著」current_max 往後比。

 若 current_max <= val：表示原先的 current_max 較小，把它放入前綴串列，改把更大的 val 作為新的局部最大值帶往下一個數字。

 將陣列第一項 arr[0] 作為起始的最大值，剩下的項目丟給 my_reduce。

 跑完一趟後，整批資料中真正的最大值一定會被推到最後，最後將 prefix 與 max_val 組合起來返回。

4. 輪數控制：取代外層迴圈

 傳統外層迴圈需要進行 N-1 次排序。

 這裡將剩餘輪數 passes 作為遞迴計數器：每次對 arr 做一次單趟冒泡 bubble_pass(arr)，並將 passes - 1 傳入下一層遞迴。

 當 passes <= 1 時終止遞迴，回傳最終已排序好的陣列。

使用 : https://share.gemini.google/pyZBoiz5gMtl


  
