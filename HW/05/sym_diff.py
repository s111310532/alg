def sym_diff(expr, var='x'):
    if isinstance(expr, (int, float)):
        return 0
    
    if isinstance(expr, str):
        return 1 if expr == var else 0

    op = expr[0]

    if op == 'sin':
        u = expr[1]
        return simplify(('*', ('cos', u), sym_diff(u, var)))

    if op == 'cos':
        u = expr[1]
        return simplify(('*', ('*', -1, ('sin', u)), sym_diff(u, var)))

    if op == 'ln':
        u = expr[1]
        return simplify(('/', sym_diff(u, var), u))

    if op == 'exp':
        u = expr[1]
        return simplify(('*', expr, sym_diff(u, var)))

    u, v = expr[1], expr[2]
    du = sym_diff(u, var)
    dv = sym_diff(v, var)

    if op == '+':
        return simplify(('+', du, dv))

    if op == '-':
        return simplify(('-', du, dv))

    if op == '*':
        return simplify(('+', ('*', du, v), ('*', u, dv)))

    if op == '/':
        numerator = ('-', ('*', du, v), ('*', u, dv))
        denominator = ('^', v, 2)
        return simplify(('/', numerator, denominator))

    if op == '^':
        if isinstance(v, (int, float)):
            coeff = ('*', v, ('^', u, v - 1))
            return simplify(('*', coeff, du))
        else:
            raise NotImplementedError

    raise ValueError(f"Unknown operator: {op}")


def simplify(expr):
    if not isinstance(expr, tuple):
        return expr

    op = expr[0]
    children = [simplify(c) for c in expr[1:]]

    if op == '+':
        u, v = children
        if u == 0: return v
        if v == 0: return u
        if isinstance(u, (int, float)) and isinstance(v, (int, float)):
            return u + v
        return ('+', u, v)

    if op == '-':
        u, v = children
        if v == 0: return u
        if u == 0: return ('*', -1, v)
        if isinstance(u, (int, float)) and isinstance(v, (int, float)):
            return u - v
        return ('-', u, v)

    if op == '*':
        u, v = children
        if u == 0 or v == 0: return 0
        if u == 1: return v
        if v == 1: return u
        if isinstance(u, (int, float)) and isinstance(v, (int, float)):
            return u * v
        return ('*', u, v)

    if op == '^':
        u, n = children
        if n == 0: return 1
        if n == 1: return u
        return ('^', u, n)

    return (op, *children)
