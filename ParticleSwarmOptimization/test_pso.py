from PSO import ParticleSwarmOptimization as PSO
import matplotlib.pyplot as plt
import numpy as np


def fitness_function(x):
    sum = (x[1] - 1)*(x[1] - 2)
#    length = len(x)
#    x = x ** 2
#    for i in range(length):
#        sum += x[i]
    return sum


my_pso = PSO(30,5)
my_pso.init_population(fitness_function)
fitness = my_pso.iteration(fitness_function,100)

plt.figure(1)
plt.title("Figure1")
plt.xlabel("iterators", size=14)
plt.ylabel("fitness", size=14)
t = np.array([t for t in range(0, 100)])
fitness = np.array(fitness)
plt.plot(t, fitness, color='b', linewidth=3)
plt.show()