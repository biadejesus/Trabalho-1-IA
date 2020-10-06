import csv
dic = {}
data = {}

with open('teste.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    result = []
    for row in reader:
         result.append(dict(row))
    print(result[0]['Low'])
    print(result[0]['High'])
