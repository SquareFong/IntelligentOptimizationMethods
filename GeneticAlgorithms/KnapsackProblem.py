from GeneticAlgorithms import GeneticAlgorithm as ga


with open("/home/squarefong/Documents/背包问题.txt", 'r') as f:
    data = f.read().split()

things = []


maxVolume = data[0]

for element in range(1, len(data), 2):
    p = []
    p.append(int(data[element]))
    p.append(int(data[element + 1]))
    things.append(p)

GA = ga(things)

ps = GA.initialize_population(100)

for i in ps:
    print(i)

# print(things)
