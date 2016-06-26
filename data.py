from math import exp, pi
import scipy as sp


ro = 34.5
a = 0.0238  # 238 * 10 ** (-4)  # * 10 ** (-6) 0.0238
C = 1  # 0.01  # 0.91
r = ro / (pi * a ** 2)  # 0.4
c = 2 * pi * a * C  # 1.5 * 10**(-7)

TIME = 10  # 10
DISTANCE = 0.6
DDSISTANCE = 0.01
DTIME = min(r * c * DDSISTANCE ** 2 / 5, 0.01)
T_COUNT = int(TIME / DTIME) + 1
X_COUNT = int(DISTANCE / DDSISTANCE) + 1

ALPHAS = {
    'm': lambda v: 0.1 * (25 - v) / (sp.exp((25 - v) / 10.) - 1),
    'h': lambda v: 0.07 * sp.exp(- v / 20.0),
    'n': lambda v: 0.01 * (10 - v) / (sp.exp((10 - v) / 10) - 1)
}

BETAS = {
    'm': lambda v: 4 * sp.exp(-v / 18),
    'h': lambda v: 1.0 / (1.0 + sp.exp((30 - v) / 10.0)),
    'n': lambda v: 0.125 * sp.exp(- v / 80)
}

# ohm^-1/ cm^2
G_NA = 120
G_K = 36
G_L = 0.3

# mV
V_boundary = 0
V_initial_impulse = 100
V_initial = 0
V_k = -12  # -11
V_na = 115  # 109
V_l = 10.5995  # 11
# ohm/cm

# micrometer
# r = ro /(pi*a**2)
# c = 2piaC
# jion = 2piaJion
# cm

# ohms/cm^2
RESISTANCE = 2 * 10**4

# microF/cm^2

# mF/cm^2
# c = 2 * pi *a *C
