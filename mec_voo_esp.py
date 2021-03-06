from math import sqrt
import numpy as np

# Constants:

mu_sol = 1.3271e11  # [km³/s²]
mu_venus = 324900  # [km³/s²]
R_terra = 149.6e6  # [km]
R_venus = 108.2e6  # [km]
r_venus = 6052  # [km]

# non-Hohmann transfer (orbit 1):

rad = 30 * np.pi / 180  # True anomaly at inbound [rad]

e1 = (R_terra - R_venus) / (R_terra + R_venus * np.cos(rad))  # Transfer orbit eccentricity
print("e1 =", round(e1, 4))

h1 = np.sqrt(mu_sol * R_terra * (1 - e1))  # [km²/s]
print("h1 =", round(h1, 2), "km²/s")

a1 = 6.684e-9 * h1**2 / (mu_sol * (1 - e1**2))
print("a1 =", round(a1, 4), "ua")

V_trans1 = h1 / R_venus  # Transverse velocity [km/s]
print("transverse vel =", round(V_trans1, 2), "km/s")

V_rad1 = (mu_sol / h1) * e1 * np.sin(-rad)  # Radial velocity [km/s]
print("radial vel =", round(V_rad1, 2), "km/s")

gamma1 = (np.arctan(V_rad1 / V_trans1)) * 180 / np.pi  # Flight path angle [º]
print("gamma =", round(gamma1, 2), "º")

V1_mod = np.sqrt(V_rad1**2 + V_trans1**2)  # Vehicle speed at the inbound crossing [km/s]
print("Inbound speed =", round(V1_mod, 2), "km/s")

# Orbital elements 1:
#
# Semimajor axis = 0.8545 ua
# Eccentricity = 0.1702
# Inclination = 0º
# Ascending node longitude = 0º
# Argument of periapsis = 0º


# Flyby through Venus (orbit 2):

V1 = np.array([V_trans1, V_rad1])  # Vehicle velocity at the inbound crossing [km/s]
print("Inbound velocity = [", round(V1[0], 4), ",", round(V1[1], 4), "] km/s")

V_venus_mod = np.sqrt(mu_sol / R_venus)  # Venus speed in circular orbit [km/s]
print("Venus speed =", round(V_venus_mod, 2), "km/s")

V_venus = np.array([V_venus_mod, 0])  # Venus velocity in circular orbit [km/s]
print("Venus velocity = [", round(V_venus[0], 4), ",", round(V_venus[1], 4), "] km/s")

V_inf = V1 - V_venus  # Hyperbolic excess vehicle velocity [km/s]
print("Hyperbolic velocity 1 = [", round(V_inf[0], 4), ",", round(V_inf[1], 4), "] km/s")

V_inf_mod = np.sqrt(V_inf[0]**2 + V_inf[1]**2)  # Hyperbolic excess vehicle speed [km/s]
print("Hyperbolic speed =", round(V_inf_mod, 2), "km/s")

rp = r_venus + 300  # Periapse radius [km]
print("Periapse radius =", round(rp, 2), "km")

h_v = rp * np.sqrt(V_inf_mod**2 + (2 * mu_venus / rp))  # Hyperbola angular momentum [km²/s]
print("Hyperbola angular momentum =", round(h_v, 2), "km²/s")

e_v = 1 + (rp * V_inf_mod**2) / mu_venus  # Hyperbola eccentricity
print("Hyperbola eccentricity =", round(e_v, 2))

deltinha = 2 * np.arcsin(1 / e_v) * 180 / np.pi  # Asymptote turn angle [º]
print("Asymptote turn angle =", round(deltinha, 2), "º")

theta_inf = np.arccos(-1 / e_v) * 180 / np.pi  # Asymptote true anomaly [º]
print("Asymptote true anomaly =", round(theta_inf, 2), "º")

delta = rp * np.sqrt((e_v + 1) / (e_v - 1))  # Aiming radius [km]
print("Aiming radius =", round(delta, 2), "km")

phi = np.arctan(-V_inf[1] / V_inf[0]) * 180 / np.pi  # Inbound velocity angle [º]
print("Inbound velocity angle =", round(phi, 2), "º")

phi2 = (phi + deltinha)  # Outbound velocity angle [º]
print("Outbound velocity angle =", round(phi2, 2), "º")

V_inf2 = V_inf_mod * np.array([np.cos(phi2 * np.pi / 180), np.sin(phi2 * np.pi / 180)])  # Hyperbolic excess vehicle velocity [km/s]
print("Hyperbolic velocity 2 = [", round(V_inf2[0], 4), ",", round(V_inf2[1], 4), "] km/s")

V2 = V_venus + V_inf2  # Vehicle heliocentric velocity at outbound [km/s]
print("Heliocentric velocity = [", round(V2[0], 4), ",", round(V2[1], 4), "] km/s")

V_trans2 = V2[0]  # Transverse velocity [km/s]
print("Transverse velocity =", round(V_trans2, 2), "km/s")

V_rad2 = V2[1]  # Radial velocity [km/s]
print("Radial velocity =", round(V_rad2, 2), "km/s")

v2 = sqrt(V_trans2**2 + V_rad2**2)  # Outbound speed [km/s]
print("Outbound speed =", round(v2, 2), "km/s")

h2 = R_venus * V_trans2
print("Momentum =", round(h2, 2), "km²/s")

e2_cos_theta2 = (h2**2 / (mu_sol * R_venus)) - 1
print("e * cos(theta) =", round(e2_cos_theta2, 4))

e2_sin_theta2 = - V_rad2 * h2 / mu_sol
print("e * sin(theta) =", round(e2_sin_theta2, 4))

theta2 = 180 + np.arctan((e2_sin_theta2 / e2_cos_theta2)) * 180 / np.pi
print("theta 2 =", round(theta2, 7), "º")

e2 = e2_cos_theta2 / np.cos(theta2 * np.pi / 180)
print("e2 =", round(e2, 4))

Rp2 = h2**2 / (mu_sol * (1 + e2))
print("Perihelium 2 =", round(Rp2, 2), "km")

a2 = 6.684e-9 * Rp2 * (1 + e2) / (1 - e2)  # Semimajor axis after flyby
print("Semimajor axis 2 =", round(a2, 4), "ua")

# Orbital elements 2:
#
# Semimajor axis = 0.7283 ua
# Eccentricity = 0.1848
# Inclination = 0º
# Longitude of the ascending node = 0º
# Argument of periapsis = 138º
