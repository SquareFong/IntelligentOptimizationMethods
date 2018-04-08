from GeneticAlgorithms import GeneticAlgorithm as ga
import math

with open("/home/squarefong/Documents/背包问题.txt", 'r') as f:
    data = f.read().split()

things = []


maxVolume = int(data[0])

for element in range(1, len(data), 2):
    p = []
    p.append(int(data[element]))
    p.append(int(data[element + 1]))
    things.append(p)

GA = ga(things)

GA.initialize_population(500)


all_fitness = []


def fitness(population, all_fitness):
    all_fitness.clear()
    for ind in range(0, len(population)):
        val = 0
        vol = 0
        individual = population[ind]
        for i in range(0, len(individual)):
            if individual[i] == 1:
                vol += things[i][0]
                val += things[i][1]
        if vol > maxVolume:
            val = math.log(val+1, 10)
        p = [ind, vol, val]
        all_fitness.append(p)


generation = 100
best = []


def is_over(best):
    max_length = len(best)-1
    if max_length > 4:
        if best[max_length][-1][2]==best[max_length - 1][-1][2] \
                and best[max_length-1][-1][2]==best[max_length-2][-1][2] \
                and best[max_length - 3][-1][2] == best[max_length - 4][-1][2] \
                and best[max_length - 4][-1][2] == best[max_length - 5][-1][2]:
            return True
    return False


gen = generation
while gen > 0:
    gen -= 1
    fitness(GA.population, all_fitness)
    GA.roulette_wheel(all_fitness)
    best.append(GA.get_best(all_fitness))
    if is_over(best) and best[-1][-1][1] < maxVolume:
        print("在经过{}次迭代后找到可能的解".format(generation-gen))
        print(best[-1][0:len(best[-1])-1],end=" ")
        print("总重量 {} 总价值 {}".format(best[-1][-1][1],best[-1][-1][2]))
        break
    GA.update_population(100)
    fitness(GA.population, all_fitness)
    GA.roulette_wheel(all_fitness)
    GA.next_generation(all_fitness)

if gen == 0:
    print("fail to find best choose")
#for i in pop:
#    print(i)

#print(all_fitness)
# print(things)
