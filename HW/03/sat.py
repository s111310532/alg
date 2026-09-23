import itertools
from typing import List, Dict, Tuple

class TruthTableSATSolver:
    def __init__(self, clauses: List[List[int]], var_names: Dict[int, str] = None):
        self.clauses = clauses
        self.vars = sorted(list({abs(lit) for clause in clauses for lit in clause}))
        self.var_names = var_names or {v: f"x{v}" for v in self.vars}

    def evaluate_clause(self, clause: List[int], assignment: Dict[int, bool]) -> bool:
        for lit in clause:
            var = abs(lit)
            val = assignment[var]
            if lit > 0 and val:
                return True
            if lit < 0 and not val:
                return True
        return False

    def evaluate_formula(self, assignment: Dict[int, bool]) -> bool:
        return all(self.evaluate_clause(c, assignment) for c in self.clauses)

    def solve_and_print_truth_table(self) -> Tuple[bool, List[Dict[int, bool]]]:
        n = len(self.vars)
        satisfying_assignments = []
        
        headers = [self.var_names[v] for v in self.vars] + ["Formula"]
        col_widths = [max(len(h), 5) for h in headers]
        
        header_row = " | ".join(f"{h:^{col_widths[i]}}" for i, h in enumerate(headers))
        separator = "-+-".join("-" * col_widths[i] for i in range(len(headers)))
        
        print("\n" + "=" * len(header_row))
        print("Truth Table Enumeration")
        print("=" * len(header_row))
        print(header_row)
        print(separator)

        for bool_tuple in itertools.product([True, False], repeat=n):
            assignment = dict(zip(self.vars, bool_tuple))
            result = self.evaluate_formula(assignment)
            
            if result:
                satisfying_assignments.append(assignment)

            row_vals = ["T" if assignment[v] else "F" for v in self.vars]
            row_vals.append("T" if result else "F")
            
            row_str = " | ".join(f"{val:^{col_widths[i]}}" for i, val in enumerate(row_vals))
            if result:
                row_str += "  <-- SATISFIES"
            print(row_str)

        print(separator)

        is_sat = len(satisfying_assignments) > 0
        if is_sat:
            print(f"\n[Result]: SATISFIABLE (SAT)")
            print(f"Total Satisfying Assignments: {len(satisfying_assignments)}")
            for idx, sol in enumerate(satisfying_assignments, 1):
                sol_str = ", ".join(f"{self.var_names[k]}={sol[k]}" for k in sorted(sol.keys()))
                print(f"  Solution {idx}: {sol_str}")
        else:
            print(f"\n[Result]: UNSATISFIABLE (UNSAT)")

        return is_sat, satisfying_assignments


if __name__ == "__main__":
    cnf_sat_example = [
        [1, -2],
        [-1, 3],
        [2, 3]
    ]
    
    print("--- Test 1: SAT Example ---")
    solver1 = TruthTableSATSolver(cnf_sat_example)
    solver1.solve_and_print_truth_table()

    cnf_unsat_example = [
        [1],
        [-1]
    ]
    
    print("\n--- Test 2: UNSAT Example ---")
    solver2 = TruthTableSATSolver(cnf_unsat_example)
    solver2.solve_and_print_truth_table()
