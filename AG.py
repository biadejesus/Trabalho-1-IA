import csv
import numpy as np
dic = {}

arquivos = ['LREN3.SA.csv', 'VIVT3.SA.csv']

for i in range(2):
    with open(arquivos[i], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        result = []
        for row in reader:
            if row['Date'][0:4] != '2016':
                result.append(dict(row))
        dic[arquivos[i]] = result
#print(dic['teste.csv'])

# 100 - (100/1+ alta/baixa)
# 14 dias a alta e fazer media e 14 dias baixa e fazer media e colocar na formula


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
        print(rsi)
        aux = 0
            
def popinicial (n):
    matriz_pop = np.random.multinomial(100, np.ones(10)/10, size=n)
    matriz_pop = [list(x) for x in matriz_pop]
    print(matriz_pop)

calcula_rsi(dic)
