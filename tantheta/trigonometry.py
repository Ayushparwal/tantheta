from sympy import Eq, solve, sin, cos, tan, symbols

def solve_trig_equation(equation_str, var_str='x'):
    x = symbols(var_str)
    expr = eval(equation_str.replace("^", "**").replace(var_str, "x"))
    eq = Eq(expr, 0)
    return solve(eq, x)
