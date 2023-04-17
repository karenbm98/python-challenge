import csv

with open ('/Resources/budget_data.csv', encoding='UTF-8') as csvfile:
    pointer = csv.reader(csvfile)
    next(pointer)
    for x in pointer:
            print(x)
