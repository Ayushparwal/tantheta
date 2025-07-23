from tantheta.chemistry import balance_equation
from tantheta.chemistry import ideal_gas_law

P = ideal_gas_law(V=5, n=2, T=300)  # Solve for Pressure
print(f"Pressure = {P:.2f} atm")

print(balance_equation("H2 + O2 = H2O"))
# Output: 2H2 + 1O2 = 2H2O

print(balance_equation("C7H6O2 + KMnO4 + H2SO4 = CO2 + MnSO4 + K2SO4 + H2O"))
# Output: 1C7H6O2 + 6KMnO4 + 9H2SO4 = 7CO2 + 6MnSO4 + 3K2SO4 + 12H2O