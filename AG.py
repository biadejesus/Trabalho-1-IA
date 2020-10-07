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
    k = 0
    result = 0
    rsi = {}
    cont=0
    aux = 0
    for i in dic:
        for j in range(len(dic[i])):
            diferenca = float(dic[i][j]['Close'])-float(dic[i][j]['Open'])
            if ( diferenca > 0 ):
                ganhos += diferenca
            else:
                perdas += -diferenca
            cont += 1
            
            if(cont == 13):
                aux += 1
                u = ganhos/14
                d = perdas/14
                if(d==0):
                    d=1
                result += 100-(100/(1+(u/d)))
                cont = 0
        rsi[i] = result/aux
        result = 0
        aux = 0
    return rsi

def fitness (rsi, individuo):
    fitness = 0
    for i in range(len(rsi)):
        fitness += rsi[arquivos[i]] * individuo[i]
    return fitness
        
def popinicial (n):
    matriz_pop = np.random.multinomial(100, np.ones(10)/10, size=n)
    matriz_pop = [list(x) for x in matriz_pop]
    #print (matriz_pop)
    return matriz_pop

def selecao(matriz_pop, rsi):
    k = 5
    result = []
    torneio = {}
    aux = {}
    geradores = {}
    while True:
        r = randint(0, len(matriz_pop)-1)
        if r not in result:
            result.append(r)
            torneio[r] = matriz_pop[r]
        if len(result) == k:
            break
    for key, i in torneio.items():
        aux[key] = fitness(rsi, i)
    geradores = sorted(aux.items(), key=itemgetter(1), reverse=True)
    return geradores[0], geradores[1]
    
def cruzamento(pai, mae):
    filho = []
    cont=0
    aux=[]
    igual = []
    soma=0
    print(pai) # tem que pegar a primeira posição do pai e pegar a posição na matriz
    # for i in range(10):
    #     filho.append(0)
    #     if(pai[i] == mae[i]):
    #         filho[i] = pai[i]
    #         soma += pai[i]
    #         igual.append(i)
    # if(len(igual) == 10):
    #     return filho
    # aux = np.random.multinomial(100 - soma , np.ones(10-len(igual))/(10-len(igual)), size=1)[0]
    # for i in range(len(filho)):
    #     if i not in igual:
    #         filho[i] = aux[cont]
    #         cont +=1
    # print(filho)
    return filho

def mutacao(filho):
    aux = []
    a = randint(0, 9)
    b = randint(0, 9)
    filho[a], filho[b] = filho[b], filho[a]
    print ('aaa ',filho)

    return filho
    
# def atualiza_pop(filho):
#     nova_pop =[]

# individuo = [10,10,10,10,10,10,10,10,10,10]
rsi = calcula_rsi(dic)
# fitness(rsi, individuo)
matriz = popinicial(10)
pai, mae = selecao(matriz, rsi)
filho = cruzamento(pai, mae)
# mutacao(filho)
