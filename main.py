import random
from tabulate import tabulate
class Individuo:
    def __init__(self, arreglo):
        self.arreglo = arreglo
        self.fitness = self.funcionFitness()
    
    def funcionFitness(self):
        x = int(self.arreglo[0:5], 2)
        y = int(self.arreglo[5:10], 2)
        return x*x*y - x*y*y
    
    def mutar(self):
        for i in range(10):
            if random.random() < 0.1:
                if self.arreglo[i] == '1':
                    self.arreglo = self.arreglo[0:i] + '0' + self.arreglo[i+1:10]
                else:
                    self.arreglo = self.arreglo[0:i] + '1' + self.arreglo[i+1:10]
        self.fitness = self.funcionFitness()

def ruleta(arr):
    total = 0
    for i in range(0, len(arr)):
        total += arr[i].fitness
    return random.choices(arr, weights=[i.fitness/total for i in arr], k = 2)

def torneo(arr, n=3):
    list = []
    for i in range(n):
        list.append(random.choice(arr))
    max = min([x.fitness for x in list])
    aux = ''
    for i in range(len(list)):
        if list[i].fitness >= max:
            max = list[i].fitness
            aux = list[i]
    return aux

def cruce(ind1, ind2):
    aux = [random.randint(0,1) for i in range(0, 10)]
    h1 = ''
    h2 = ''
    for i in range(0,len(aux)):
        if aux[i] == 1:
            h1 = h1+((ind2.arreglo[i]))
            h2 = h2+((ind1.arreglo[i]))
        else:
            h1 = h1+((ind1.arreglo[i]))
            h2 = h2+((ind2.arreglo[i]))
    return Individuo(h1), Individuo(h2)

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

def max_fitness(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i].fitness > max:
            max = arr[i].fitness
    return max, arr[i].arreglo

def main():
    n = 4
    tab = []
    pobla = generarPoblacion(n)
    gen = 0
    while gen < 100:
        aux = []
        for i in range(0,int(n/2)):
            a = torneo(pobla, 3)
            b = torneo(pobla, 3)
            x,y = cruce(a,b)
            x.mutar()
            y.mutar()
            aux.append(x)
            aux.append(y)
        pobla = aux
        x = ['Generación: ', gen+1, ' Max: ', max_fitness(aux)[0]]
        tab.append(x)
        gen+=1
    print(tab)
    print('final: ', max_fitness(pobla))

main()
