from decimal import *
from data import *
import matplotlib.pyplot as plt

print(X_COUNT)
print(T_COUNT)


def make_matrix():
    return [[0 for i in range(X_COUNT)] for j in range(T_COUNT)]
ms = make_matrix()
ns = make_matrix()
hs = make_matrix()
vs = make_matrix()

# Начални условия
for i in range(X_COUNT):
    vs[0][i] = V_initial
    ms[0][i] = ALPHAS['m'](vs[0][
                           i]) / (ALPHAS['m'](vs[0][i]) + BETAS['m'](vs[0][i]))

    ns[0][i] = ALPHAS['n'](vs[0][
                           i]) / (ALPHAS['n'](vs[0][i]) + BETAS['n'](vs[0][i]))

    hs[0][i] = ALPHAS['h'](vs[0][
                           i]) / (ALPHAS['h'](vs[0][i]) + BETAS['h'](vs[0][i]))

# Първият допълнителен импулс
for i in range(10):
    vs[0][i] = V_initial_impulse

# Гранични условия в левия и десния ъгъл на матрицата
for j in range(T_COUNT):
    vs[j][0] = V_boundary

# Попълваме матрицата
for j in range(1, T_COUNT):
    for i in range(1, X_COUNT - 1):
        ms[j][i] = ms[j - 1][i] + DTIME * (ALPHAS['m'](vs[j - 1][i]) - ms[j - 1][i] * (
            ALPHAS['m'](vs[j - 1][i]) + BETAS['m'](vs[j - 1][i])))
        ns[j][i] = ns[j - 1][i] + DTIME * (ALPHAS['n'](vs[j - 1][i]) - ns[j - 1][i] * (
            ALPHAS['n'](vs[j - 1][i]) + BETAS['n'](vs[j - 1][i])))
        hs[j][i] = hs[j - 1][i] + DTIME * (ALPHAS['h'](vs[j - 1][i]) - hs[j - 1][i] * (
            ALPHAS['h'](vs[j - 1][i]) + BETAS['h'](vs[j - 1][i])))

        Jion = G_K * ns[j - 1][i]**4 * (vs[j - 1][i] - V_k) + \
            G_NA * ms[j - 1][i]**3 * hs[j - 1][i] * (vs[j - 1][i] - V_na) + \
            G_L * (vs[j - 1][i] - V_l)

        jion = 2 * pi * a * Jion
        jion /= c
        coeff = 1 / (r * c) / DDSISTANCE ** 2
        second_derivative = coeff * \
            (vs[j - 1][i + 1] - 2 * vs[j - 1][i] + vs[j - 1][i - 1])

        vs[j][i] = vs[j - 1][i] + DTIME * (second_derivative - jion)
    vs[j][X_COUNT-1] = DTIME / (r * c) * (vs[j-1][X_COUNT-1] * (r * c / DTIME) + vs[j-1][X_COUNT-1] - jion)

#print(ns)
# print(vs)
ts = [i * DDSISTANCE for i in range(X_COUNT)]
for k in range(1000):
    vs_plot = [vs[k][i] for i in range(X_COUNT)]
    fig = plt.plot(ts, vs_plot, 'ro')
    plt.savefig('{}.png'.format(k))
    plt.close()
