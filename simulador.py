import csv
# import numpy as np
dic = {}
capInicial = 100000
arquivos = ['CIEL3.SA.csv','CSNA3.SA.csv','GRND3.SA.csv', 'JSLG3.SA.csv', 'LEVE3.SA.csv', 'LREN3.SA.csv', 'SBSP3.SA.csv', 'UGPA3.SA.csv', 'VIVT3.SA.csv', 'WEGE3.SA.csv' ]

for i in range(10):
    with open(arquivos[i], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        result = []
        for row in reader:
            if row['Date'][0:4] == '2016':
                result.append(dict(row))
        dic[arquivos[i]] = result


def final(investimentos, carteira):
    fim = 0
    for i in investimentos:
        fim+=float(investimentos[i])
    fim+=carteira
    print("-----------------------   Resultado da simulacao  --------------------------------------\n")
    print("\t\tO valor final foi de: ", fim)
    if fim - capInicial < 0:
        print("\t\tPerdas: ", fim - capInicial)
    else:
        print("\t\tGanhos: ", fim - capInicial)
    return fim
        


def calc_rsi(investimentos, carteira):
    mes = {}
    x = []
    aux3 = []
    soma = 0
    cont=0
    aux = 0
    aux2 = 0
    for i in dic:
        for j in range(len(dic[i])):
            soma += float(dic[i][j]['Close'])
            cont+=1
            if(cont == 14):
                media = soma/cont+1
                if media > float(dic[i][j]['Close']):
                    carteira += float(investimentos[i]) * float(dic[i][j]['Close'])
                    investimentos[i] = 0
                    x = [dic[i][j]['Date'], investimentos[i], carteira]
                    print(aux3.append(x))
                    mes[i] = aux3.append(dic[i][j]['Date'])

                else:
                    if carteira >= float(dic[i][j]['Close']):
                        print("COmpra")
                        aux = carteira//float(dic[i][j]['Close']) 
                        aux2 = float(dic[i][j]['Close']) * aux
                        print(aux2)
                        carteira -= aux2
                        investimentos[i] = aux
                        x = [dic[i][j]['Date'], investimentos[i], carteira]
                        mes[i] = aux3.append(x)
                cont = 0
                soma = 0
                media = 0

    return investimentos, carteira, mes

def inicializa(invInic):
    aux = 0
    carteira = 0
    invInic = {x: float(invInic[x]/100)* capInicial for x in invInic}
    for i in dic:
        aux = invInic[i]//float(dic[i][0]['Close']) 
        aux2 = float(dic[i][0]['Close']) * aux
        carteira += invInic[i] - aux2
        invInic[i] = aux
        #simulador(invInic, carteira)
    # print(invInic)
    # print(carteira)
    return invInic, carteira


investimentos, carteira = inicializa({'WEGE3.SA.csv': 10, 'VIVT3.SA.csv': 10, 'UGPA3.SA.csv': 10,'SBSP3.SA.csv': 10,'LREN3.SA.csv': 10,'LEVE3.SA.csv': 10,'JSLG3.SA.csv': 10,'GRND3.SA.csv': 10,'CSNA3.SA.csv': 10,'CIEL3.SA.csv': 10})
investimentos, carteira, mes = calc_rsi(investimentos, carteira)
fim = final(investimentos, carteira)
# print(investimentos)
# print(carteira)
print(mes)
print(fim)
