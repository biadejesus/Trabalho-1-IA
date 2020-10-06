import csv
#import numpy as np

dic = {}
qtd = 1
arquivos = ['LREN3.SA.csv']

for i in range(1):
    with open(arquivos[i], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        result = []
        for row in reader:
            if row['Date'][0:4] == '2016':
                result.append(dict(row))
        dic[arquivos[i]] = result


def verifica(invInic):
    for i in dic:
        for j in range(len(dic[i])):
            x = float(dic[i][j]["Close"]) - float(dic[i][j]["Open"])
             



def simulador(invInic):
    print(invInic['WEGE3.SA.csv'])
    capInicial = 100000
    for x in invInic:
        print(invInic[x])
    invInic = {x: float(invInic[x]/100)* capInicial for x in invInic}
    print(invInic)
    verifica(invInic)

print(dic)
print(len(dic))
simulador({'WEGE3.SA.csv': 10, 'VIVT3.SA.csv': 5, 'UGPA3.SA.csv': 3,'SBSP3.SA.csv':2,'LREN3.SA.csv': 20,'LEVE3.SA.csv': 10,'JSLG3.SA.csv': 10,'GRND3.SA.csv': 10,'CSNA3.SA.csv': 10,'CIEL3.SA.csv': 10})
