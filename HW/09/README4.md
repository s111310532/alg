NPC 搜尋玩家問題

一.A*

A* 依據評估函數f(n)來決定下一個優先展開的節點：f(n) = g(n) + h(n)

1.g(n)：從起點到節點n的累計實際移動代價。

2.h(n)：從節點n到終點的預估代價。

3.f(n)：經過節點n到達玩家的綜合預估花費。優先展開f(n)最小的節點。

h(n)的選取規則

1.四方向移動:使用曼哈頓距離

h(n)=∣x_n ​- x_target ​∣ + ∣ y_n ​- y_target ​∣

2.八方向移動：使用切比雪夫距離或對角線距離

h(n)=Δx+Δy+(√2​−2)⋅min(Δx,Δy)

3.任意角度：使用歐幾里得距離

h(n)= √(x _n ​− x_target ​) ^2 + (y_n ​− y_target ​) ^2 ​

使用:https://share.gemini.google/LaP1TTk0GEtE
