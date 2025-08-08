from tantheta.physics import (
    solve_kinematics,
    projectile_motion,
    work_energy_theorem,
    centripetal_force,
    lens_formula,
    magnification,
    convert_units,
    ohms_law,
    coulombs_law,
    wave_speed,
    shm_motion,
    phy_ideal_gas_law,
    photon_energy,
    de_broglie_wavelength,
    impulse,
    torque,
    gravitational_force,
    capacitance,
    inductive_reactance,
    magnetic_force,
    doppler_effect,
    heat_transfer,
    carnot_efficiency,
    relativistic_mass,
    time_dilation,
    escape_velocity,
    orbital_period,
    schwarzschild_radius,
    buoyant_force,
    bernoulli_pressure,
    viscosity_force,
    magnetic_flux,
    induced_emf,
    inductance,
    work_done_pressure_volume,
    efficiency,
    entropy_change,
    de_broglie_frequency,
    uncertainty_position,
    half_life
)

print(solve_kinematics(u=10, a=2, t=5))
print(projectile_motion(u=20, angle=45))
print(work_energy_theorem(m=5, u=10, v=20))
print(centripetal_force(m=2, v=10, r=5))

print(lens_formula(u=10, v=15))
print(magnification(height_image=5, height_object=10))
print(convert_units("90 deg to rad"))

print(ohms_law(i=2, r=5))
print(coulombs_law(q1=1e-6, q2=2e-6, r=0.5))

print(wave_speed(frequency=50, wavelength=0.2))
print(shm_motion(amplitude=5, angular_freq=2, time=1))

print(phy_ideal_gas_law(P=101325, V=0.1, n=4, T=None))
print(photon_energy(frequency=5e14))
print(de_broglie_wavelength(mass=9.11e-31, velocity=2.2e6))

print(impulse(force=10, time=2))
print(torque(force=5, distance=2))
print(gravitational_force(m1=5.97e24, m2=7.35e22, r=3.84e8))

print(capacitance(charge=1e-6, voltage=10))
print(inductive_reactance(frequency=50, inductance=0.1))
print(magnetic_force(q=1.6e-19, v=1e6, B=0.01))

print(doppler_effect(frequency=1000, velocity_source=30, velocity_observer=0))
print(heat_transfer(mass=2, specific_heat=900, delta_temp=10))
print(carnot_efficiency(T_hot=500, T_cold=300))

print(relativistic_mass(rest_mass=9.11e-31, velocity=2e8))
print(time_dilation(proper_time=1, velocity=2e8))

print(escape_velocity(mass=5.97e24, radius=6.371e6))
print(orbital_period(mass_central=1.989e30, radius=1.496e11))
print(schwarzschild_radius(mass=1.989e30))

print(buoyant_force(density_fluid=1000, volume_submerged=0.5))
print(bernoulli_pressure(p1=101325, v1=5, h1=10, v2=10, h2=5, density=1.225))
print(viscosity_force(viscosity=0.001, area=0.01, velocity_gradient=100))

print(magnetic_flux(B=0.01, area=1))
print(induced_emf(B=0.01, length=2, velocity=3))
print(inductance(n_turns=100, magnetic_flux=1e-6, current=0.01))

print(work_done_pressure_volume(P_initial=101325, V_initial=1, P_final=100000, V_final=2))
print(efficiency(work_done=500, heat_supplied=1000))
print(entropy_change(heat_transferred=500, temperature=300))

print(de_broglie_frequency(energy=3.3e-19))
print(uncertainty_position(momentum_uncertainty=1e-24))
print(half_life(decay_constant=0.0001))
