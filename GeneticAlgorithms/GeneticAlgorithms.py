import random


class GeneticAlgorithm:
    def __init__(self, data):
        self.data = data
        self.population = []
        self.wheel = []
        self.population_size = 0

    def initialize_population(self, population_size):
        self.population_size = population_size
        data_size = len(self.data)
        if len(self.population) != 0:
            self.population.clear()
        for i in range(0,population_size):
            individual = []
            for j in range(0,data_size):
                individual.append(random.randint(0, 1))
            self.population.append(individual)
        return self.population

    def roulette_wheel(self, all_fitness):
        #all_fitness.sort(key=lambda x: x[2], reverse=True)
        wheel = []
        total_fitness = 0.0
        for i in all_fitness:
            total_fitness += i[2]
        f = 0.0
        for i in all_fitness:
            f += i[2]
            wheel.append(f/total_fitness)
        self.wheel = wheel
        return wheel

    def pickup_individual(self, wheel):
        s = random.random()
        i, j = 0, len(wheel)-1
        while i + 1 < j:
            m = int((i + j) / 2)
            if wheel[m] >= s:
                j = m
            else:
                i = m
        return self.population[i]

    def mutation(self):
        i = self.population_size * 0.10
        j = int(len(self.population[0]) * 0.3)
        size = len(self.population) - 1
        length = len(self.population[0])-1
        while i >= 0:
            for t in range(j):
                ind = random.randint(0, size)
                pos = random.randint(0, length)
                self.population[ind][pos] ^= 1
            i -= 1

    def update_population(self, generations):
        i = generations
        while i > 0:
            i -= 1
            individual1, individual2 = self.pickup_individual(self.wheel), self.pickup_individual(self.wheel)
            cut = random.randint(0,len(self.population[0]) - 1)
            self.population.append(individual1[0:cut] + individual2[cut:])
            self.population.append(individual2[0:cut] + individual1[cut:])
        return self.population

    def next_generation(self, all_fitness):
        pop_size = self.population_size
        self.roulette_wheel(all_fitness)
        pop = []
        while pop_size > 0:
            pop.append(self.pickup_individual(self.wheel))
            pop_size -= 1
        self.population = pop
        return self.population

    def get_best(self, all_fitness):
        max_val, max_val_i = 0.0, 0
        for i in range(0, len(self.wheel)-1):
            if all_fitness[i][2] > max_val:
                max_val = all_fitness[i][2]
                max_val_i = i
        return self.population[max_val_i] + [all_fitness[max_val_i],]