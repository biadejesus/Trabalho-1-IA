import csv
import numpy as np
dic = {}

arquivos = ['LREN3.SA.csv', 'teste.csv']

for i in range(2):
    with open(arquivos[i], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        result = []
        for row in reader:
            if row['Date'][0:4] != '2016':
                result.append(dict(row))
        dic[arquivos[i]] = result
print(dic['teste.csv'][10])

# 100 - (100/1+ U/D)


# def calcula_rsi(dic):
#     for 


def popinicial (n):
    matriz_pop = np.random.multinomial(100, np.ones(10)/10, size=n)
    matriz_pop = [list(x) for x in matriz_pop]
    print(matriz_pop)

popinicial(10)

