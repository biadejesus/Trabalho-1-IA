import csv
dic = {}

with open('teste.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dic = {'teste':(row['Low'], row['High'])}

    print(dic)