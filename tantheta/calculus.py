from sympy import symbols, limit, diff, integrate, sin, cos, tan, ln, exp, oo, sympify

x = symbols('x')

def find_limit(expr: str, point: float):
    expr_sym = sympify(expr)
    return limit(expr_sym, x, point)

def differentiate(expr: str):
    expr_sym = sympify(expr)
    return diff(expr_sym, x)

def integration(expr: str):
    expr_sym = sympify(expr)
    return integrate(expr_sym, x)
