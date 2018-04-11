from PSO import ParticleSwarmOptimization as PSO
import matplotlib.pyplot as plt
import numpy as np


def fitness_function(x):
    sum = 0#(x[1] - 1)*(x[1] - 2)
    length = len(x)
    for i in range(length - 1):
        sum += ((1-x[i])**2 + 100 * ((x[i+1] - x[i]**2)**2))
    return sum


iterator = 100
my_pso = PSO(100, 5)
my_pso.init_population(fitness_function, 0.0, 1.0, 0, 60)
fitness = my_pso.iteration(fitness_function,iterator)

plt.figure(1)
plt.title("Figure1")
plt.xlabel("iterators", size=14)
plt.ylabel("fitness", size=14)
t = np.array([t for t in range(0, iterator)])
fitness = np.array(fitness)
plt.plot(t, fitness, color='b', linewidth=2)
plt.show()
