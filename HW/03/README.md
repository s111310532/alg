Truth Table SAT Solver

一個基於系統性枚舉（Brute-force Enumeration）真值表的布林可滿足性問題（Boolean Satisfiability Problem, SAT）求解器。

核心設計理念本專案使用標準的 合取範式（CNF, Conjunctive Normal Form） 來表示命題邏輯公式：

*公式由多個子句（Clause）以邏輯 AND 連接而成。
*每個子句由一或多個文字（Literal）以邏輯 OR 連接而成。
*變數使用正整數編號（如 1, 2, 3 代表變數 $x_1, x_2, x_3$）。
*負整數代表否定（如 -2 代表 $\neg x_2$）。

演算法流程

1.變數擷取：掃描所有子句，提取並排序所有唯一的正整數變數識別碼。
2.窮舉賦值：利用 Python 內建的 itertools.product([True, False], repeat=n) 產生所有可能的 $2^n$ 種布林變數指派。
3.子句與公式評估：
  *對於特定指派，若子句中至少有一個文字的值為 True，該子句即判定為真。
  *若所有子句皆為真，則整份公式判定為真。
4.輸出真值表與結果：將每一步指派結果格式化印出，標註滿足解（Satisfying Assignments），並回傳公式是否為 SAT 或 UNSAT。

程式碼結構解析

類別 / 方法	功能說明
TruthTableSATSolver.__init__	接收 CNF 子句集合，自動推導所有出現的變數集合，並建立變數名稱對應表。
evaluate_clause	傳入單一子句與目前的布林賦值字典，判定子句是否滿足（OR 運算）。
evaluate_formula	檢查公式中所有子句是否均為真（AND 運算）。
solve_and_print_truth_table	走訪所有真值表列，列印對齊的真值表，記錄滿足解，並輸出 SAT/UNSAT 總結。

測試案例與驗證

測試案例 1：可滿足問題 (SAT)
輸入公式

cnf_sat_example = [
    [1, -2],     # (x1 ∨ ¬x2)
    [-1, 3],     # (¬x1 ∨ x3)
    [2, 3]       # (x2 ∨ x3)
]
對應邏輯式：(x 1 ​ ∨¬x 2 ​ )∧(¬x 1 ​ ∨x 3 ​ )∧(x 2 ​ ∨x 3 ​)

驗證結論：共有 3 組滿足解：

1.x 1 ​ =True,x 2 ​ =True,x 3 ​ =True 
2.x 1 ​ =True,x 2 ​ =False,x 3 ​ =True 
3.x 1 ​ =False,x 2 ​ =False,x 3 ​ =True

測試案例 2：不可滿足問題 (UNSAT)
輸入公式

cnf_unsat_example = [
    [1],     # (x1)
    [-1]     # (¬x1)
]
對應邏輯式：x 1 ​ ∧¬x 1 ​

驗證結論：無任何指派可使公式為真，判定為 UNSATISFIABLE (UNSAT)。

終端機預期輸出

--- Test 1: SAT Example ---

================================
Truth Table Enumeration
================================
 x1   |  x2   |  x3   | Formula
------+-------+-------+--------
  T   |   T   |   T   |    T     <-- SATISFIES
  T   |   T   |   F   |    F   
  T   |   F   |   T   |    T     <-- SATISFIES
  T   |   F   |   F   |    F   
  F   |   T   |   T   |    F   
  F   |   T   |   F   |    F   
  F   |   F   |   T   |    T     <-- SATISFIES
  F   |   F   |   F   |    F   
-------------------------------

[Result]: SATISFIABLE (SAT)
Total Satisfying Assignments: 3
  Solution 1: x1=True, x2=True, x3=True
  Solution 2: x1=True, x2=False, x3=True
  Solution 3: x1=False, x2=False, x3=True

--- Test 2: UNSAT Example ---

=========================
Truth Table Enumeration
=========================
  x1   | Formula
-------+--------
   T   |    F   
   F   |    F   
------------------------

[Result]: UNSATISFIABLE (UNSAT)

複雜度分析與限制時間複雜度：
1.時間複雜度:
  *其中n為變數數量，m為子句數量。
  *每增加一個變數，枚舉次數呈現指數倍（*2）成長。

2.適用邊界：
  *本程式適用於n≤20的教學與小型邏輯驗證。
  *若變數規模超過 30，真值表列數將突破 10 億列，實務上應改用 DPLL、CDCL 等現代 SAT 求解演算法。
