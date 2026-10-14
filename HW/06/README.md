Lambda calculus 

解譯器具備以下特點:

1.支援變數、λ抽象與函數呼叫。

2.在代換時遇到同名變數自動進行 α-轉換。

3.最左最外層優先化簡。

4.印出每一次 β-規約與必要 α-轉換的完整過程。

測試程式與執行輸出

1.布林邏輯：NOT TRUE 

2.Church 數值與加法運算：ADD 1 1 

3.避免變數捕捉：(\x. \y. x) y 

4.無窮遞迴：Ω = (λx.x x) (λx.x x) 

# Church 巨集常數定義

TRUE = r"(\x. \y. x)"

FALSE = r"(\x. \y. y)"

NOT = f"(\\b. b {FALSE} {TRUE})"

ZERO = r"(\f. \x. x)"

ONE = r"(\f. \x. f x)"

PLUS = r"(\m. \n. \f. \x. m f (n f x))"

# 1. 布林運算: NOT TRUE
evaluate(f"({NOT} {TRUE})")

# 2. 避免變數捕捉 (α-conversion 觸發)
evaluate(r"(\x. \y. x) y")

# 3. Church 數值加法: 1 + 1 -> 2 (\f. \x. f (f x))
evaluate(f"({PLUS} {ONE} {ONE})")

# 4. 無窮迴圈 Omega 測試
evaluate(r"(\x. x x) (\x. x x)", max_steps=4)

執行結果

=================================================================
輸入表達式: ((\b. b (\x. \y. y) (\x. \y. x)) (\x. \y. x))
=================================================================
Step 0: ((λb. ((b (λx. (λy. y))) (λx. (λy. x)))) (λx. (λy. x)))
   β-step: Replace 'b' with '(λx. (λy. x))'
Step 1: (((λx. (λy. x)) (λx. (λy. y))) (λx. (λy. x)))
   β-step: Replace 'x' with '(λx. (λy. y))'
Step 2: ((λy. (λx. (λy. y))) (λx. (λy. x)))
   β-step: Replace 'y' with '(λx. (λy. x))'
Step 3: (λx. (λy. y))

>> 達到正規形式 (Normal Form)！
最終結果: (λx. (λy. y))   <-- 即 FALSE

=================================================================
輸入表達式: (\x. \y. x) y
=================================================================
Step 0: ((λx. (λy. x)) y)
   β-step: Replace 'x' with 'y'
   [α-conversion] Renaming 'y' to 'y_1' in (λy. x)
Step 1: (λy_1. y)

>> 達到正規形式 (Normal Form)！
最終結果: (λy_1. y)

=================================================================
輸入表達式: (\x. x x) (\x. x x)
=================================================================
Step 0: ((λx. (x x)) (λx. (x x)))
   β-step: Replace 'x' with '(λx. (x x))'
Step 1: ((λx. (x x)) (λx. (x x)))
   β-step: Replace 'x' with '(λx. (x x))'
Step 2: ((λx. (x x)) (λx. (x x)))
   β-step: Replace 'x' with '(λx. (x x))'
Step 3: ((λx. (x x)) (λx. (x x)))
   β-step: Replace 'x' with '(λx. (x x))'
Step 4: ((λx. (x x)) (λx. (x x)))

>> 超過最大步數限制 (4 steps)，計算停止（可能為無窮迴圈）。
最終結果: ((λx. (x x)) (λx. (x x)))
