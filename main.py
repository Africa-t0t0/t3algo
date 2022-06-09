import random

class Individuo:
    def __init__(self, arreglo):
        self.arreglo = arreglo
        self.fitness = self.funcionFitness()
    
    def funcionFitness(self):
        x = int(self.arreglo[0:5], 2)
        y = int(self.arreglo[5:10], 2)
        if y > x:
            return 1
        return x*x*y - x*y*y
    
    def mutar(self):
        for i in range(10):
            if random.random() < 0.01:
                if self.arreglo[i] == 1:
                    self.arreglo[i] = 0
                else:
                    self.arreglo[i] = 1
        self.fitness = self.funcionFitness(self.arreglo)

def ruleta(arr):
    total = 0
    for i in range(0, len(arr)):
        total += arr[i].fitness
    return random.choices(arr, weights=[i.fitness/total for i in arr], k = 2)

def cruce(ind1, ind2):
    pass

def generarPoblacion(n):
    ind = []
    for i in range(n):
        a = random.randint(0,31)
        b = random.randint(0,31)
        a = bin(a)[2:] 
        b = bin(b)[2:]
        while (len(a) < 5):
            a = '0' + a
        while (len(b) < 5):
            b = '0' + b
        ind.append(Individuo(a+b))
    return ind

x,y = ruleta(generarPoblacion(100))

print(x.fitness, y.fitness)