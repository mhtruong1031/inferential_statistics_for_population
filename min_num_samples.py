from adjusted_prop_popsamplingdist import PopulationSamplingDistribution
import numpy as np
from math import sqrt
from os import system
import matplotlib.pyplot as plt

# Returns population confidence interval
def get_population_conf_int(p_estimate, std) -> tuple:
    interval = 1.960 * (std/(sqrt(abs(p_estimate))))

    return (p_estimate-interval, p_estimate+interval)

# Return second order sampling distribution statistics
def get_second_order_distribution(N: int):
    estimated_population = []
    bmean                = []
    pmean                = []
    amean                = []
    means                = []
    stds                 = []

    in_intervals = 0
    for i in range(1000):
        dist = PopulationSamplingDistribution(N = pop)
        for j in range(700):
            dist.generate_distribution(500)
        
        p_estimate = dist.get_population_point_estimate()
        interval   = dist.get_population_conf_int()
        estimated_population.append(p_estimate)
        if interval[0] <= p_estimate and p_estimate <= interval[1]:
            in_intervals += 1
        mean = np.mean(dist.succ)
        std  = np.std(dist.succ)

        if mean >= 29 and mean <= 29.5:
            bmean.append(std)
        if mean >= 29.75 and mean <= 30.25:
            pmean.append(std)
        if mean >= 30.5 and mean <= 31:
            amean.append(std)

        means.append(mean)
        stds.append(std)

        if i % 1000 == 0:
            print(f"{i} 2nd Order Distributions Created")
    
    perc_conf = in_intervals / 1000
    
    bin_size = 100
    hist, bins = np.histogram(estimated_population, bins=range(-40000,40000, bin_size))

    return (estimated_population, means, stds, bmean, pmean, amean, perc_conf)

pop = 1000
system('clear')

est, means, stds, bmean, pmean, amean, perc_conf = get_second_order_distribution(pop)

figure, axis = plt.subplots(2, 3)

print(est)

print(f'b-n: {len(bmean)}')
print(f'p-n: {len(pmean)}')
print(f'a-n: {len(amean)}')

print(f'b-mean: {np.mean(bmean)}')
print(f'p-mean: {np.mean(pmean)}')
print(f'a-mean: {np.mean(amean)}')

print(f'b-std: {np.std(bmean)}')
print(f'p-std: {np.std(pmean)}')
print(f'a-std: {np.std(amean)}')

print(f'mean est: {np.mean(est)}')
print(f'std est: {np.std(est)}')
print(f'conf-int: {get_population_conf_int(np.mean(est), np.std(est))}')
print(f'percent in interval: {perc_conf}')

axis[0,0].hist(est, range=(-20000,20000), bins=200)
axis[0,0].set_title("Estimated Population")

axis[0,1].hist(means, range=(28, 32), bins=100)
axis[0,1].set_title("Means")

axis[0,2].hist(stds, range=(4, 5), bins=100)
axis[0,2].set_title("Standard Deviations")

axis[1,0].hist(bmean, range=(4, 5), bins=100)
axis[1,0].set_title("Below Means STD")

axis[1,1].hist(pmean, range=(4, 5), bins=100)
axis[1,1].set_title("Point Means STD")

axis[1,2].hist(amean, range=(4, 5), bins=100)
axis[1,2].set_title("Above Means STD")  

plt.show()