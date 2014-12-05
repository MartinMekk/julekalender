__author__ = 'martinsolheim'

filename = "/Users/martinsolheim/Desktop/julekalender/kilma_data_blindern.txt"

results = []
with open(filename, newline='\n') as inputFile:
    for line in inputFile:
        results.append(line.strip().split())
inputFile.close()
minValue = 100
date = "00.00.00"


def month_reader(a_date):
    split_date = a_date.split('.')
    if split_date[1] == '12':
        return 12
    else:
        return -1

for line in results:
    tempValue = float(line[3].replace(',','.'))
    tempDate = month_reader(line[1])
    if tempDate == 12 and tempValue < minValue:
        minValue = tempValue
        date = line[1]


print(minValue, date)