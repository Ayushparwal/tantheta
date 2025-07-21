import tantheta
from tantheta.calculus import find_limit, differentiate, integration, definite_integral, partial_derivative, second_derivative,taylor_series,find_critical_points
from tantheta.algebra import dot_product, cross_product, classify_conic,factor_expression,expand_expression, solve_linear_equation, solve_linear_system,is_polynomial, degree_of_polynomial
from tantheta.probability import nPr, nCr, basic_probability
from tantheta.stats import mean, median, variance, standard_deviation
from tantheta.trigonometry import (
    solve_trig_equation,
    simplify_trig_expression,
    expand_trig_expression,
    factor_trig_expression,
    evaluate_trig_identity,
    verify_trig_identity,
    is_trig_identity
)

print(tantheta.add(4, 5))      
print(tantheta.subtract(9, 3)) 
print(tantheta.multiply(4,4))  
# print(tantheta.divide(4,0))    

print(find_limit("sin(x)/x", 0)) 

expr = "x**3 + 2*x**2 + 5*x + 7"
derivative = differentiate(expr)
print("Derivative:", derivative)

expr = "x*sin(x)"
integral = integration(expr)
print("Integral:", integral)

v1 = [1, 2, 3]
v2 = [4, 5, 6]

result = dot_product(v1, v2)
print("Dot Product:", result)

v1 = [1, 0, 0]
v2 = [0, 1, 0]

result = cross_product(v1, v2)
print("Cross Product:", result)

examples = [
    "x^2 + y^2 - 25",
    "x^2 - y^2 - 4",
    "x^2 + 4*y",
    "x^2 + 3*y^2 + 2*x*y - 10",
    "sin(x) + y"
]

for expr in examples:
    result = classify_conic(expr)
    print(f"{expr} ➜ {result}")
    
print(nCr(5, 2))
print(nPr(5, 2))
print(basic_probability(3, 10))
print(nCr(3, 5))
print(nPr(3, 5))

data = [5, 10, 15, 10, 20]
print(mean(data))               # 12.0
print(median(data))             # 10
print(variance(data))           # 26.0
print(standard_deviation(data)) 

solution = solve_trig_equation("sin(x) - 0.5")
print(solution) 

print(second_derivative("x**3 + 2*x"))
print(partial_derivative("x**2 + y**2", "y"))
print(definite_integral("x**2", 0, 2))
print(taylor_series("sin(x)", 0, 5))
print(find_critical_points("x**3 - 3*x + 2"))

print(factor_expression("x**2 - 9"))             # (x - 3)(x + 3)
print(expand_expression("(x + 2)**2"))           # x**2 + 4x + 4
print(solve_linear_equation("2*x + 3 - 5"))      # x = 1
print(solve_linear_system(["2*x + y = 4", "x - y = 1"], ['x', 'y']))  # {'x': 5/3, 'y': 2/3}
print(is_polynomial("x**3 + 2*x"))               # False
print(degree_of_polynomial("x**3 + 2*x")) 

# 1. Solving a basic trigonometric equation
print(solve_trig_equation("sin(x) - 1/2"))
# Output: [pi/6, 5*pi/6]

# 2. Simplifying a trigonometric identity
print(simplify_trig_expression("sin(x)**2 + cos(x)**2"))
# Output: 1

# 3. Expanding a compound angle formula
print(expand_trig_expression("sin(x + y)"))
# Output: sin(x)*cos(y) + cos(x)*sin(y)

# 4. Factoring a trigonometric expression
print(factor_trig_expression("sin(x)*cos(x) + cos(x)**2*sin(x)"))
# Output: sin(x)*cos(x)*(1 + cos(x))

# 5. Evaluating a known identity for truth
print(evaluate_trig_identity("tan(x) - sin(x)/cos(x)"))
# Output: True

# 6. Verifying that two expressions are equivalent
print(verify_trig_identity("1 - 2*sin(x)**2", "cos(2*x)"))
# Output: True

# 7. Checking whether a complex expression is an identity
print(is_trig_identity("sin(x)**4 + 2*sin(x)**2*cos(x)**2 + cos(x)**4 - 1"))
# Output: True