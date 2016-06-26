import json
from data_threshold import *
from data import DTIME
import os
from time import sleep

offset = 12

leading_edge = [[] for i in range(number_axons)]
for n in range(number_axons):
    with open('voltage{}.json'.format(n), 'r') as outfile:
        vs = json.loads(outfile.read())
    leading_edge[n] = [vs[i].index(max(vs[i])) for i in range(len(vs))]

#print(leading_edge)

axon_length = len(vs[0]) - offset

for i in range(len(leading_edge[0])):
    for j in range(len(leading_edge)):
        max_index = leading_edge[j][i]
        axon_string = '-' * (max_index - 1) + '*' + '-' * (axon_length - max_index - 1)
        print(axon_string)
    sleep(0.8)
    os.system('clear')
