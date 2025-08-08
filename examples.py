import tantheta
from tantheta.calculus import second_derivative, partial_derivative, definite_integral
from tantheta.maths import ap_nth_term, gp_sum, triangle_area, is_prime, prime_factors
from tantheta.physics import solve_kinematics, projectile_motion, ohms_law, coulombs_law, wave_speed
from tantheta.chemistry import balance_equation, ideal_gas_law, molarity, pH

# Calculus examples
print("Second derivative:", second_derivative("x**3 + 2*x"))
print("Partial derivative wrt y:", partial_derivative("x**2 + y**2", "y"))
print("Definite integral of x^2 from 0 to 2:", definite_integral("x**2", 0, 2))

# Maths examples
print("AP 5th term:", ap_nth_term(2, 3, 5))          # 2 + (5-1)*3 = 14
print("GP sum first 4 terms:", gp_sum(3, 2, 4))      # 3*(2^4-1)/(2-1) = 45
print("Triangle area (3,4,5):", triangle_area(3,4,5))
print("Is 17 prime?", is_prime(17))
print("Prime factors of 28:", prime_factors(28))

# Physics examples
print("Solve kinematics:", solve_kinematics(u=0, a=9.8, t=5))
print("Projectile motion (u=20, angle=30):", projectile_motion(20, 30))
print("Ohm's law voltage:", ohms_law(i=2, r=5))
print("Coulomb force:", coulombs_law(q1=1e-6, q2=2e-6, r=0.5))
print("Wave speed:", wave_speed(frequency=50, wavelength=0.2))

# Chemistry examples
print("Balanced equation:", balance_equation("H2 + O2 = H2O"))
print("Ideal gas law (solve for P):", ideal_gas_law(V=5, n=2, T=300))
print("Molarity of 2 moles in 1 L:", molarity(2, 1))
print("pH of H+ concentration 1e-7:", pH(1e-7))
