import csv
dic = {}
data = {}

with open('teste.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    n = 0
    for row in reader:
        n+=1
        data[row] = {}
       # print(row['Low'], row['High'])
        for line in reader:
             data[row][line[0]] = line[n]

print(data)    