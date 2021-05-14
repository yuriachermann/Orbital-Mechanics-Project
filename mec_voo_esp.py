# Code developed by Luiz Junior in 05/12/2021 at 11:18

from math import sqrt
import numpy as np
import sympy as s

# Constants:
mu_sol = (1.3271)*(10**11) # Em km^3/s^2

mu_venus = 324900 # Em km^3/s^2

R_terra = (149.6)*(10**6) # Em km

R_venus = (108.2)*(10**6) # Em km

r_venus = 6052 # Em km

# Fase 1 da missao:

degress = 30*np.pi/180

e1 = (R_terra-R_venus)/(R_terra+R_venus*np.cos(degress))

h1 = np.sqrt(mu_sol*R_terra*(1-e1)) # Em km^2/s

V_par = h1/R_venus # Em km/s

V_r = (mu_sol/h1)*e1*np.sin(degress) # Em km/s

#print(V_par)
#print(V_r)

gamma = (np.arctan(V_r/V_par))*180/np.pi 

#print(gamma)

v1v = np.sqrt(V_r**2+V_par**2) # Em km/s

#print(v1v)

# Fase 2 da missao (Flyby para venus):

V1 = np.array((V_par,V_r))

# The velocity of Venus in its presumed circular orbit around the sun is

V_venus = np.sqrt(mu_sol/R_venus)

# print(V_venus) # ok

V = np.array((V_venus,0))

V_inf = V1-V

# disto temos que

v_inf = np.sqrt(V_inf[0]*V_inf[0]+V_inf[1]*V_inf[1])

#print(v_inf) ok

rp = r_venus+300

h_v = rp*np.sqrt(v_inf**2+(2*mu_venus/rp))

e_v = 1 + (rp*(v_inf**2))/mu_venus

deltinha = 2*s.asin(1/e_v)*180/np.pi

theta_inf = s.acos(-1/e_v)*180/np.pi

delta = rp*np.sqrt((e_v+1)/(e_v-1)) # Em km

# angle between v_inf e V

fi = s.atan(V_inf[1]/V_inf[0])*180/np.pi

#print(fi)

fi2_deg = (fi + deltinha)

fi2 = (fi + deltinha)*np.pi/180

V_inf2 = v_inf*np.array((s.cos(fi2),s.sin(fi2)))

V2 = V + V_inf2

V_par2 = V2[0]

V_r2 = V2[1]

#The speed of the spacecraft at the outbound crossing is

v2 = sqrt(V_par2**2+V_r2**2) #km/s

# Fim do calculo para o dark side
