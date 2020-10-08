import csv
import copy
import numpy as np

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


def calcula_porcentagem(inicial, final):
    return ((final - inicial) /
            inicial) * 100

def final(investimentos, carteira, mes, carteiraI, inicial):
    fim = 0
    for i in investimentos:
        fim+=float(carteira[i])

    print("-----------------------   Resultado da simulacao  --------------------------------------\n")
    print("\t\tO valor incial foi de: 100000")
    print("\t\tO valor final foi de: ", fim)
    if fim - capInicial < 0:
        print("\t\tPerdas: ", fim - 100000)
    else:
        print("\t\tGanhos: ", fim - 100000)
    print("\n----------------------------   Ganho mensal  --------------------------------------\n")
    meses2 = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio' , 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    soma = 0
    soma2 = 0

    for j in range(12):
        soma += mes['CIEL3.SA.csv'][j][0] + mes['CIEL3.SA.csv'][j][1]
        soma += mes['CSNA3.SA.csv'][j][0] + mes['CSNA3.SA.csv'][j][1]
        soma += mes['GRND3.SA.csv'][j][0] + mes['GRND3.SA.csv'][j][1]
        soma += mes['JSLG3.SA.csv'][j][0] + mes['JSLG3.SA.csv'][j][1]
        soma += mes['LEVE3.SA.csv'][j][0] + mes['LEVE3.SA.csv'][j][1]
        soma += mes['LREN3.SA.csv'][j][0] + mes['LREN3.SA.csv'][j][1]
        soma += mes['SBSP3.SA.csv'][j][0] + mes['SBSP3.SA.csv'][j][1]
        soma += mes['UGPA3.SA.csv'][j][0] + mes['UGPA3.SA.csv'][j][1]
        soma += mes['VIVT3.SA.csv'][j][0] + mes['VIVT3.SA.csv'][j][1]
        soma += mes['WEGE3.SA.csv'][j][0] + mes['WEGE3.SA.csv'][j][1]

        if j == 0:
            lucro = copy.deepcopy(float(soma)- 100000.0)
            aux = copy.deepcopy(lucro)
            aux = str(aux)
            print("\t\t"+meses2[j] + ": "+aux)
            soma = 0
        else:
            soma2 += mes['CIEL3.SA.csv'][j-1][0] + mes['CIEL3.SA.csv'][j-1][1]
            soma2 += mes['CSNA3.SA.csv'][j-1][0] + mes['CSNA3.SA.csv'][j-1][1]
            soma2 += mes['GRND3.SA.csv'][j-1][0] + mes['GRND3.SA.csv'][j-1][1]
            soma2 += mes['JSLG3.SA.csv'][j-1][0] + mes['JSLG3.SA.csv'][j-1][1]
            soma2 += mes['LEVE3.SA.csv'][j-1][0] + mes['LEVE3.SA.csv'][j-1][1]
            soma2 += mes['LREN3.SA.csv'][j-1][0] + mes['LREN3.SA.csv'][j-1][1]
            soma2 += mes['SBSP3.SA.csv'][j-1][0] + mes['SBSP3.SA.csv'][j-1][1]
            soma2 += mes['UGPA3.SA.csv'][j-1][0] + mes['UGPA3.SA.csv'][j-1][1]
            soma2 += mes['VIVT3.SA.csv'][j-1][0] + mes['VIVT3.SA.csv'][j-1][1]
            soma2 += mes['WEGE3.SA.csv'][j-1][0] + mes['WEGE3.SA.csv'][j-1][1]
            lucro = copy.deepcopy(float(soma) - float(soma2))
            aux = copy.deepcopy(lucro)
            aux = str(aux)
            print("\t\t"+meses2[j] + ": "+aux)
            soma = 0
            soma2 = 0     

    print("\n----------------------------   Ganhos e perdas das ações  --------------------------------------\n")
    for i in inicial:
        result = int(calcula_porcentagem(inicial[i], carteira[i]))
        print("\t\t"+i,": ",str(result)+"%")

         


def calc_media(investimentos, carteira):
    mes = {}
    x = [0,0,0,0,0,0,0,0,0,0,0,0]
    soma = 0
    cont=0
    aux = 0
    aux2 = 0

    for i in dic:
        for j in range(len(dic[i])):
            soma += float(dic[i][j]['Close'])
            cont+=1
            if(cont == 45):
                media = soma/cont+1
                if media > float(dic[i][j]['Close']):
                    carteira[i] += copy.deepcopy(float(investimentos[i]) * float(dic[i][j]['Close']))
                    investimentos[i] = 0 
                else:
                    if float(carteira[i]) >= float(dic[i][j]['Close']):
                        aux = copy.deepcopy(float(carteira[i])//float(dic[i][j]['Close']))
                        aux2 = copy.deepcopy(float(dic[i][j]['Close']) * aux)
                        carteira[i] -= copy.deepcopy(aux2)
                        investimentos[i] += copy.deepcopy(aux)
                cont = 0
                media = 0
                soma = 0
            if int(dic[i][j]['Date'][5:7]) != 12: 
                if ( int(dic[i][j]['Date'][5:7]) < (int(dic[i][j+1]['Date'][5:7]))):
                    x[(int(dic[i][j]['Date'][5:7]))-1] = copy.deepcopy([carteira[i], investimentos[i]*float(dic[i][j]['Close'])])
                    mes[i] = copy.deepcopy(x)
            elif j == len(dic[i])-1:
                x[(int(dic[i][j]['Date'][5:7]))-1] = copy.deepcopy([carteira[i], investimentos[i]*float(dic[i][j]['Close'])])
                mes[i] = copy.deepcopy(x)
    return investimentos, carteira, mes

def inicializa(invInic):
    aux = 0
    inicial = 0
    carteira = {'WEGE3.SA.csv': 0, 'VIVT3.SA.csv': 0, 'UGPA3.SA.csv': 0,'SBSP3.SA.csv': 0,'LREN3.SA.csv': 0,'LEVE3.SA.csv': 0,'JSLG3.SA.csv': 0,'GRND3.SA.csv': 0,'CSNA3.SA.csv': 0,'CIEL3.SA.csv': 0}
    invInic = {x: float(invInic[x]/100)* capInicial for x in invInic}
    inicial = copy.deepcopy(invInic)
    for i in dic:
        aux = copy.deepcopy(invInic[i]//float(dic[i][0]['Close']))
        aux2 = copy.deepcopy(float(dic[i][0]['Close']) * aux)
        carteira[i] += copy.deepcopy(invInic[i] - aux2)
        invInic[i] = copy.deepcopy(aux)
    return invInic, carteira, inicial

entrada = {'LREN3.SA.csv': 5, 'VIVT3.SA.csv': 11, 'CIEL3.SA.csv': 5, 'CSNA3.SA.csv': 17, 'GRND3.SA.csv': 11, 'WEGE3.SA.csv': 5, 'JSLG3.SA.csv': 18, 'LEVE3.SA.csv': 13, 'SBSP3.SA.csv': 14, 'UGPA3.SA.csv': 1}

def simula(entrada):
    investimentos, carteira, inicial = copy.deepcopy(inicializa(entrada))
    investI = copy.deepcopy(investimentos)
    carteiraI = copy.deepcopy(carteira)
    investimentos, carteira, mes = copy.deepcopy(calc_media(investimentos, carteira))
    fim = copy.deepcopy(final(investimentos, carteira, mes, carteiraI, inicial))

