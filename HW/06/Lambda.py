import re

# ==========================================
# 1. 語法樹節點定義 (AST)
# ==========================================
class Term:
    pass

class Var(Term):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

class Abs(Term):
    def __init__(self, param: str, body: Term):
        self.param = param
        self.body = body

    def __str__(self):
        return f"(λ{self.param}. {self.body})"

class App(Term):
    def __init__(self, func: Term, arg: Term):
        self.func = func
        self.arg = arg

    def __str__(self):
        return f"({self.func} {self.arg})"

# ==========================================
# 2. 詞法與語法分析器 (Lexer & Parser)
# 語法規則:
#   Expr  := Lam | AppExpr
#   Lam   := ('\' | 'λ') Var '.' Expr
#   AppExpr := Atom+ (左結合)
#   Atom  := Var | '(' Expr ')'
# ==========================================
def tokenize(s: str):
    # 支援語法符號: \, λ, ., (, ) 與變數名稱
    token_spec = r'λ|\\|\.|\(|\)|[a-zA-Z0-9_]+'
    return re.findall(token_spec, s)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected=None):
        token = self.peek()
        if expected and token != expected:
            raise SyntaxError(f"Expected '{expected}', found '{token}'")
        self.pos += 1
        return token

    def parse(self) -> Term:
        term = self.parse_expr()
        if self.pos < len(self.tokens):
            raise SyntaxError(f"Unexpected token: {self.peek()}")
        return term

    def parse_expr(self) -> Term:
        tok = self.peek()
        if tok in ('\\', 'λ'):
            self.consume()
            param = self.consume()
            self.consume('.')
            body = self.parse_expr()
            return Abs(param, body)
        return self.parse_app()

    def parse_app(self) -> Term:
        atoms = []
        while self.peek() and self.peek() not in (')', '.', '\\', 'λ'):
            atoms.append(self.parse_atom())
        if not atoms:
            raise SyntaxError(f"Unexpected token in application: {self.peek()}")
        # 函數調用為左結合: e1 e2 e3 => ((e1 e2) e3)
        res = atoms[0]
        for arg in atoms[1:]:
            res = App(res, arg)
        return res

    def parse_atom(self) -> Term:
        tok = self.peek()
        if tok == '(':
            self.consume('(')
            expr = self.parse_expr()
            self.consume(')')
            return expr
        elif tok and re.match(r'[a-zA-Z0-9_]+', tok):
            return Var(self.consume())
        raise SyntaxError(f"Unexpected atom token: {tok}")

def parse(s: str) -> Term:
    return Parser(tokenize(s)).parse()

# ==========================================
# 3. 變數代換 (Capture-avoiding Substitution)
# ==========================================
def free_variables(term: Term) -> set:
    if isinstance(term, Var):
        return {term.name}
    elif isinstance(term, Abs):
        return free_variables(term.body) - {term.param}
    elif isinstance(term, App):
        return free_variables(term.func) | free_variables(term.arg)
    return set()

_counter = 0
def fresh_var(base: str) -> str:
    global _counter
    _counter += 1
    return f"{base}_{_counter}"

def substitute(term: Term, var_name: str, replacement: Term, log: list) -> Term:
    """計算 term[var_name := replacement]"""
    if isinstance(term, Var):
        return replacement if term.name == var_name else term

    elif isinstance(term, Abs):
        # 陰影效應（Shadowing）：已被內層抽象繫結
        if term.param == var_name:
            return term

        # 若替換項目的自由變數包含抽象的參數，必須進行 α-轉換避免變數被捕捉
        if term.param in free_variables(replacement):
            new_param = fresh_var(term.param)
            log.append(f"  [α-conversion] Renaming '{term.param}' to '{new_param}' in {term}")
            new_body = substitute(term.body, term.param, Var(new_param), log)
            return Abs(new_param, substitute(new_body, var_name, replacement, log))

        return Abs(term.param, substitute(term.body, var_name, replacement, log))

    elif isinstance(term, App):
        return App(
            substitute(term.func, var_name, replacement, log),
            substitute(term.arg, var_name, replacement, log)
        )

# ==========================================
# 4. 正規序規約引擎 (Normal-Order Reduction)
# ==========================================
def reduce_step(term: Term, log: list):
    """嘗試執行單步最左最外層規約 (One-step Normal-order β-reduction)"""
    if isinstance(term, App):
        # 最外層 Redex: (λx. e1) e2
        if isinstance(term.func, Abs):
            log.append(f"β-step: Replace '{term.func.param}' with '{term.arg}'")
            reduced = substitute(term.func.body, term.func.param, term.arg, log)
            return reduced, True
        
        # 先化簡左側
        new_func, changed = reduce_step(term.func, log)
        if changed:
            return App(new_func, term.arg), True
        
        # 左側無法化簡，再化簡右側
        new_arg, changed = reduce_step(term.arg, log)
        if changed:
            return App(term.func, new_arg), True

    elif isinstance(term, Abs):
        new_body, changed = reduce_step(term.body, log)
        if changed:
            return Abs(term.param, new_body), True

    return term, False

def evaluate(expr_str: str, max_steps: int = 50):
    print("=" * 65)
    print(f"輸入表達式: {expr_str}")
    print("=" * 65)
    term = parse(expr_str)
    step = 0
    print(f"Step 0: {term}")

    while step < max_steps:
        logs = []
        term, changed = reduce_step(term, logs)
        if not changed:
            print("\n>> 達到正規形式 (Normal Form)！")
            break
        step += 1
        for msg in logs:
            print(f"   {msg}")
        print(f"Step {step}: {term}")
    else:
        print(f"\n>> 超過最大步數限制 ({max_steps} steps)，計算停止（可能為無窮迴圈）。")
    print(f"最終結果: {term}\n")
