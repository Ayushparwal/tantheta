import tantheta
from tantheta.calculus import find_limit, differentiate, integration
from tantheta.algebra import dot_product, cross_product, classify_conic
from tantheta.probability import nPr, nCr, basic_probability
from tantheta.stats import mean, median, variance, standard_deviation
from tantheta.trigonometry import solve_trig_equation

print(tantheta.add(4, 5))      # Output: 9
print(tantheta.subtract(9, 3)) # Output: 6
print(tantheta.multiply(4,4))  # Output: 16
# print(tantheta.divide(4,0))    # Output: Error

print(find_limit("sin(x)/x", 0)) # Output: 1

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



