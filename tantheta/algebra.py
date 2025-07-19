from sympy import Matrix, symbols, Eq, sympify

def dot_product(v1: list, v2: list):
    return sum(a * b for a, b in zip(v1, v2))

def cross_product(v1: list, v2: list):
    return Matrix(v1).cross(Matrix(v2))

def classify_conic(expr: str) -> str:
    x, y = symbols('x y')
    expr = expr.replace('^', '**')
    try:
        poly = sympify(expr).as_poly(x, y)

        A = poly.coeff_monomial(x**2)
        B = poly.coeff_monomial(x * y)
        C = poly.coeff_monomial(y**2)

        Δ = B**2 - 4 * A * C

        if Δ == 0:
            return "Parabola"
        elif Δ > 0:
            return "Hyperbola"
        elif Δ < 0:
            if A == C and B == 0:
                return "Circle"
            return "Ellipse"
    except Exception:
        return "Not a valid conic expression"

