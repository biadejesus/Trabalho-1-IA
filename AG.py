import csv
import numpy as np
from random import randint
from operator import itemgetter


dic = {}

arquivos = ['LREN3.SA.csv', 'VIVT3.SA.csv', 'CIEL3.SA.csv', 'CSNA3.SA.csv', 'GRND3.SA.csv', 'WEGE3.SA.csv', 'JSLG3.SA.csv', 'LEVE3.SA.csv', 'SBSP3.SA.csv', 'UGPA3.SA.csv']

for i in range(len(arquivos)):
    with open(arquivos[i], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        result = []
        for row in reader:
            if row['Date'][0:4] != '2016':
                result.append(dict(row))
        dic[arquivos[i]] = result

def calcula_rsi(dic):
    ganhos = 0
    perdas = 0
    result = 0
    rsi = {}
    cont=0
    aux = 0
    for i in dic:
        for j in range(len(dic[i])-1):
            diferenca = float(dic[i][j+1]['Close'])-float(dic[i][j]['Close'])
            if ( diferenca > 0 ):
                ganhos += diferenca
            else:
                perdas += (-1) * diferenca
            cont += 1
            
            if(cont == 13):
                aux += 1
                u = ganhos/14
                d = perdas/14
                if(d==0):
                    d=1
                result += 100-(100/(1+(u/d)))
                
                cont = 0
                ganhos = 0
                perdas = 0
        rsi[i] = result/aux
        result = 0
        aux = 0
    return rsi

def fitness (rsi, individuo):
    fitness = 0
    for i in range(len(rsi)):
        fitness += (100 - rsi[arquivos[i]]) * individuo[i]
    return fitness
        
def popinicial (n):
    matriz_pop = np.random.multinomial(100, np.ones(10)/10, size=n)
    matriz_pop = [list(x) for x in matriz_pop]
    populacao = {}
    for i in range(len(matriz_pop)):
        populacao[i] = matriz_pop[i]
    return populacao

def selecao(populacao, rsi):
    k = 5
    result = []
    torneio = {}
    aux = {}
    geradores = {}
    while True:
        r = randint(0, len(populacao)-1)
        if r not in result:
            result.append(r)
            torneio[r] = populacao[r]
        if len(result) == k:
            break
    for key, i in torneio.items():
        aux[key] = fitness(rsi, i)
    geradores = sorted(aux.items(), key=itemgetter(1), reverse=True)
    return geradores[0], geradores[1]
    
def cruzamento(pai, mae, populacao):
    filho = []
    cont=0
    aux=[]
    igual = []
    soma=0
    
    for i in range(len(populacao)):
        if pai[0] == i:
            pai = populacao[i]
        if mae[0] == i:
            mae = populacao[i]
    for i in range(10):
        filho.append(0)
        if(pai[i] == mae[i]):
            filho[i] = pai[i]
            soma += pai[i]
            igual.append(i)
    if(len(igual) == 10):
        return filho
    aux = np.random.multinomial(100 - soma , np.ones(10-len(igual))/(10-len(igual)), size=1)[0]
    for i in range(len(filho)):
        if i not in igual:
            filho[i] = aux[cont]
            cont +=1
    return filho

def mutacao(filho):
    a = randint(0, 9)
    b = randint(0, 9)
    filho[a], filho[b] = filho[b], filho[a]
    return filho

def atualiza_pop(filho, rsi, populacao):

    fit_pop = {}
    fit_filho = fitness(rsi, filho)
    for i in range(len(populacao)):
        fit_pop[i] = fitness(rsi, populacao[i])
    fit_pop = sorted(fit_pop.items(), key=itemgetter(1), reverse=True)
    if fit_filho > fit_pop[len(fit_pop)-1][1]:
        populacao[fit_pop[len(fit_pop)-1][0]] = filho
    return populacao

rsi = calcula_rsi(dic)
populacao = popinicial(1000)

def ag(populacao):
    n =0
    resultado = {}
    while n < 1000:
        fit_pop={}
        pai, mae = selecao(populacao, rsi)
        filho = cruzamento(pai, mae, populacao)
        filho = mutacao(filho)
        pop = atualiza_pop(filho, rsi, populacao)
        if(n % 10 == 0):
            for i in range(len(pop)):
                fit_pop[i] = fitness(rsi, pop[i])
            fit_pop = sorted(fit_pop.items(), key=itemgetter(1), reverse=True)
            resultado = pop[fit_pop[0][0]]
        n+=1
    final = {}
    k=0
    for i in resultado:
        final[arquivos[k]] = i
        k+=1
    print(final)       

ag(populacao)

