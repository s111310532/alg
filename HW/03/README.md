Truth Table SAT Solver

探究是否存在一種解釋能夠滿足給定的布林公式。
公式中的變數是否可以一致地替換為 TRUE 或 FALSE 值，從而使公式的值為 TRUE。如果可以，則稱該公式為可滿足的；否則，稱該公式為不可滿足的。

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

