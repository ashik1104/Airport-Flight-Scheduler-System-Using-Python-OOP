import csv

with open('./Data/My_Friends.csv', 'r') as file:
    lines = csv.reader(file)
    header = next(lines)
    for line in lines:
        print(line)
    print(header)
