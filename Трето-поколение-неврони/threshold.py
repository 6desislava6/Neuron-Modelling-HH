import json
from data_threshold import *
from data import DTIME

voltages = [[] for i in range(number_axons)]
for n in range(number_axons):
    with open('voltage{}.json'.format(n), 'r') as outfile:
        vs = json.loads(outfile.read())
    voltages[n] = [vs[i][-2] for i in range(len(vs))]

# Това е масив от сумите за всяко време от теглата * векторите
sums = [sum(list(map(lambda x: x[0] * x[1], (zip(voltages[i], weights))))) for i in range(len(voltages))]

integral_formula = lambda begin, end, sums: sum(sums[begin:end])

integrals = [None for i in range(number_axons)]

for i in range(number_axons):
    t0_index = i
    tend_index = i + int(tend / DTIME)
    print(t0_index, tend_index)
    integrals[i] = integral_formula(t0_index, tend_index, sums)

print(integrals)
