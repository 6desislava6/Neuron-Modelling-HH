import random

delta_time = 0.1
number_axons = 10
range_weight = [-0.5, 0.5]
weights = [random.uniform(range_weight[0], range_weight[1]) for i in range(number_axons)]
t0 = 0
tend = 0.01
threshold = 80
