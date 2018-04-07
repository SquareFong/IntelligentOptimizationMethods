import random


class GeneticAlgorithm:
    def __init__(self, data):
        self.data = data
        self.population = []

    def initialize_population(self, population_size):
        data_size = len(self.data)
        if len(self.population) != 0:
            self.population.clear()
        for i in range(0,population_size):
            individual = []
            for j in range(0,data_size):
                individual.append(random.randint(0, 1))
            self.population.append(individual)
        return self.population

