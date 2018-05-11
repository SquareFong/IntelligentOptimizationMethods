from GeneticAlgorithms import GeneticAlgorithm as ga
import math
import os

def fitness(population, all_fitness, things, maxVolume):
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


def is_over(best):
    max_length = len(best)-1
    if max_length > 4:
        if best[max_length][-1][2]==best[max_length - 1][-1][2] \
                and best[max_length-1][-1][2]==best[max_length-2][-1][2] \
                and best[max_length - 3][-1][2] == best[max_length - 4][-1][2] \
                and best[max_length - 4][-1][2] == best[max_length - 5][-1][2]:
            return True
    return False


population_size = 1000


def test(path):
    with open(path, 'r') as f:
        answer_data = f.read().split()

    things = []
    maxVolume = int(answer_data[0])

    for element in range(1, len(answer_data), 2):
        p = [int(answer_data[element]), int(answer_data[element + 1])]
        things.append(p)
    GA = ga(things)
    GA.initialize_population(population_size)
    all_fitness = []
    generation = 100
    best = []
    gen = generation
    while gen > 0:
        gen -= 1
        fitness(GA.population, all_fitness, things, maxVolume)
        GA.roulette_wheel(all_fitness)
        best.append(GA.get_best(all_fitness))
        if is_over(best) and best[-1][-1][1] < maxVolume:
            # 输出具体结果信息
            # print("在经过{}次迭代后找到可能的解".format(generation-gen))
            # print(best[-1][0:len(best[-1])-1],end=" ")
            # print("总重量 {} 总价值 {}".format(best[-1][-1][1],best[-1][-1][2]))
            break
        GA.update_population(population_size)
        #GA.mutation() #变异
        fitness(GA.population, all_fitness, things, maxVolume)
        #GA.roulette_wheel(all_fitness)
        GA.next_generation(all_fitness)

    # if gen == 0:
    #     print("fail to find best choose")

    return best[-1]


rebootTimes = 50
print("种群大小{}，每组数据次数为{}：".format(population_size, rebootTimes))
#test("./test/1.txt")
L = os.listdir("./test/")
with open("./test/answer.txt", 'r') as f:
    data = f.read().split()
answer = dict()
for element in range(0, len(data), 2):
    answer[data[element]] = int(data[element+1])
for file in L:
    if '0' < file[0] < '9':
        print("testing file {}".format(file))

        bests = []
        for i in range(rebootTimes):
                temp = test("./test/"+file)
                if type(temp) == list:
                    bests.append(temp)
        #temp = bests[0]
        #b = 0
        # if len(bests) > 0:
        #     for i in range(len(bests)):
        #         if bests[i][-1][2] > temp[-1][2]:
        #             temp = bests[i]
        #             b = i
        #     print("经过{}次重启，找到可能的最优解：{} 总重量：{} 总价值：{}".format(b,temp[0:-1],temp[-1][1],temp[-1][2]))
        right = 0
        for result in bests:
            if result[-1][-1] == answer[file]:
                right += 1
        print("在{}次测试中，总计{}次找出最优解，成功率{}".format(rebootTimes,right, float(right)/rebootTimes))
        print('\n')
