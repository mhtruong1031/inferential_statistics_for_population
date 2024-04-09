from popsamplingdist import PopulationSamplingDistribution
import numpy as np
from os import system
import matplotlib.pyplot as plt

# Return the minimum number of samples needed
pop = 500
system('clear')

min_sample_num = []
ratios         = []

for n in range(1, pop+1):
    ratios.append(n/pop)
    dist = PopulationSamplingDistribution(N = pop)

    for num_samples in range(1, pop+1):
        for i in range(n):
            dist.generate_distribution(n)
        error = (dist.get_population_point_estimate() - pop)/pop
        if abs(error) <= .1 or num_samples == pop:
            min_sample_num.append(num_samples)
            break

plt.plot(ratios, min_sample_num)
plt.xlabel("Ratio of sample size to population")
plt.ylabel("Min numbers of samples for 10% Error")
plt.show()

print(f"mean: {np.mean(dist.props)}")
print(f"std: {np.std(dist.props)}")

print(f"point estimate: {dist.get_population_point_estimate()}")

