# Core operations
from .core import add, subtract, multiply, divide

# Algebra module
from .algebra import (
    dot_product,
    cross_product,
    classify_conic,
    factor_expression,
    expand_expression,
    solve_linear_equation,
    solve_linear_system,
    is_polynomial,
    degree_of_polynomial,
)

# Calculus module
from .calculus import (
    differentiate,
    integration,
    find_limit,
    definite_integral,
    partial_derivative,
    second_derivative,
    taylor_series,
    find_critical_points,
)

# Probability module
from .probability import (
    nPr,
    nCr,
    basic_probability,
)

# Statistics module
from .stats import (
    mean,
    median,
    variance,
    standard_deviation,
)

# Trigonometry module
from .trigonometry import (
    solve_trig_equation,
    simplify_trig_expression,
    expand_trig_expression,
    factor_trig_expression,
    evaluate_trig_identity,
    verify_trig_identity,
    is_trig_identity,
)
