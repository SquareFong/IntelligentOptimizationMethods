import numpy as np
import random



class ParticleSwarmOptimization():
    def __init__(self, m, d):
        self.w = 0.8
        self.c1 = 2
        self.c2 = 2
        self.xi = 0.6
        self.eta = 0.3
        #m个粒子，d维向量
        self.m = m
        self.d = d
        #所有粒子的位置X[0]即第一个粒子的位置
        self.X = np.zeros((m, d))
        #所有粒子的速度V[0]即第一个粒子的位置
        self.V = np.zeros((m, d))
        #所有粒子的经过的历史最好点
        self.P = np.zeros((m, d))
        #全局最佳位置
        self.best_position = np.zeros(d)
        #每个个体的最佳适应值
        self.best_fitness = np.zeros(m)
        #全局最佳适应值
        self.most_fit = 1e10

    def init_population(self, fitness_function, x_left=0.0, x_right=1.0, v_left=0.0, v_right=1.0):
        for i in range(self.m):
            for d in range(self.d):
                self.X[i][d] = random.uniform(x_left, x_right)
                self.V[i][d] = random.uniform(v_left, v_right)
            self.best_position = self.X[i]
            self.best_fitness[i] = fitness_function(self.X[i])
            if self.most_fit > self.best_fitness[i]:
                self.most_fit = self.best_fitness[i]
                self.best_position = self.X[i]

    def iteration(self, fitness_function, times):
        fitness = []
        for t in range(times):
            for i in range(self.m):
                temp = fitness_function(self.X[i])
                if temp < self.best_fitness[i]:
                    self.best_fitness[i] = temp
                    self.P[i] = self.X[i]
                    if temp < self.most_fit:
                        self.best_position = self.X[i]
                        self.most_fit = temp
            for i in range(self.m):
                self.V[i]=self.w*self.V[i] + \
                          self.c1*self.xi*(self.P[i] - self.X[i]) + \
                          self.c2*self.eta*(self.best_position - self.X[i])
                self.X[i] = self.X[i] + self.V[i]
            fitness.append(self.most_fit)
            print(self.most_fit)
        print(self.best_position)
        return fitness
