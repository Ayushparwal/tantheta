from tantheta.chemistry import (
    molarity, molality, normality, dilution, percent_composition,
    pH, pOH, pH_from_pOH, pOH_from_pH,
    equilibrium_constant,
    rate_constant, reaction_rate,
    enthalpy_change, heat,
    combined_gas_law,
    moles_to_particles, particles_to_moles,
    balance_equation,
    ideal_gas_law,
    partial_pressure, daltons_law,
    standard_cell_potential, nernst_equation,
    empirical_formula, molecular_formula,
    gibbs_free_energy, equilibrium_from_gibbs,
    beer_lambert_law,
    mole_fraction, mass_percent,
    henderson_hasselbalch, average_atomic_mass,
    heat_phase_change, arrhenius_rate_constant,
    grams_to_moles, moles_to_grams,
    partial_molar_volume, ka_from_pka
)

# Stoichiometry
print("Molarity:", molarity(0.5, 2))  # 0.25 mol/L
print("Molality:", molality(0.5, 1))  # 0.5 mol/kg
print("Normality:", normality(1, 1))  # 1 eq/L
print("Dilution (find C2):", dilution(2, 3, V2=6))  # 1.0 M
print("Percent Composition:", percent_composition(10, 50))  # 20.0 %

# Acids & Bases
print("pH:", pH(1e-4))  # 4.0
print("pOH:", pOH(1e-10))  # 10.0
print("pH from pOH:", pH_from_pOH(5))  # 9.0
print("pOH from pH:", pOH_from_pH(9))  # 5.0

# Equilibrium
print("Equilibrium constant:", equilibrium_constant([0.3, 0.2], [0.4, 0.5], [1, 2], [1, 1]))

# Reaction Kinetics
print("Rate constant (1st order half-life 20s):", rate_constant(20))
print("Reaction rate:", reaction_rate(0.1, 0.2))

# Thermochemistry
print("Enthalpy change:", enthalpy_change([400, 300], [200, 150]))
print("Heat:", heat(None, 2, 4.18, 10))  # q = mcΔT

# Gas Laws
print("Combined Gas Law (find P2):", combined_gas_law(1, 1, 300, V2=2, T2=400))
print("Moles to Particles:", moles_to_particles(2))
print("Particles to Moles:", particles_to_moles(1.2044e24))

# Balancing Equation
print(balance_equation("H2 + O2 = H2O"))
print(balance_equation("C7H6O2 + KMnO4 + H2SO4 = CO2 + MnSO4 + K2SO4 + H2O"))

# Ideal Gas Law
print("Ideal Gas Law (find P):", ideal_gas_law(V=5, n=2, T=300))

# Gas Mixtures
print("Partial Pressure:", partial_pressure(1, 0.21))
print("Dalton's Law total pressure:", daltons_law([0.2, 0.3, 0.5]))

# Electrochemistry
print("Standard Cell Potential:", standard_cell_potential(1.1, 0.4))
print("Nernst Equation:", nernst_equation(1.1, 2, 0.1))

# Advanced Stoichiometry
print("Empirical Formula ratios:", empirical_formula([12, 32], [12, 16]))
print("Molecular Formula ratios:", molecular_formula([1, 2], 60, 30))

# More Thermodynamics
print("Gibbs Free Energy:", gibbs_free_energy(-40, 0.1, 298))
print("Equilibrium from Gibbs:", equilibrium_from_gibbs(-40000))

# Spectroscopy
print("Beer-Lambert Law (absorbance):", beer_lambert_law(molar_absorptivity=20000, concentration=0.01, path_length=1))

# Solution Properties
print("Mole Fraction:", mole_fraction(2, 10))
print("Mass Percent:", mass_percent(5, 50))
print("Henderson-Hasselbalch pH:", henderson_hasselbalch(4.76, 0.1, 0.05))
print("Average Atomic Mass:", average_atomic_mass([12, 13], [0.989, 0.011]))

# Phase Change
print("Heat Phase Change:", heat_phase_change(10, 334))  # melting ice (latent heat)

# Arrhenius Equation
print("Arrhenius Rate Constant:", arrhenius_rate_constant(1e12, 50000, 298))

# Mass & Moles conversions
print("Grams to Moles:", grams_to_moles(18, 18))
print("Moles to Grams:", moles_to_grams(1, 18))

# Partial Molar Volume
print("Partial Molar Volume:", partial_molar_volume(50, [10, 20], [0.3, 0.7]))

# Acid Dissociation Constant
print("Ka from pKa:", ka_from_pka(4.76))
