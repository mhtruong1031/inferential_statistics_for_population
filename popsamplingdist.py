from random import choice, randint
import numpy as np

class PopulationSamplingDistribution():
    def __init__(self, N: int) -> None:
        self.N          = N
        self.n          = 0
        self.population = [choice([0, 1]) for i in range(N)]

        self.props      = []
        self.succ       = []

    def reset(self) -> None:
        self.n, self.props, self.succ = 0, [], []

    def generate_distribution(self, n: int) -> None:
        sample          = [self.population.pop(randint(0, len(self.population)-1)) for i in range(n)] # n samples from self.population hypogeometrically
        successes       = len(list(filter(lambda x: x == 1, sample))) # Record successes

        self.props.append(successes/n)
        self.succ.append(successes)

        self.population += sample  # Redistribute into population
        self.n          = n

    def get_population_point_estimate(self) -> float:
        mean = np.mean(self.succ)
        std  = np.std(self.succ)

        population = (std**2 + (mean * (mean - self.n))) / (std**2 + (mean / self.n) * (mean - self.n))

        return population

    def get_population_conf_int(self, conf_level: float) -> tuple:
        pass

