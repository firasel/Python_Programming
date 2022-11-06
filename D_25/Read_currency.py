import csv

with open('./data/currencyrates.csv', 'r') as file:
    lines = csv.reader(file)
    for line in lines:
        if 'Bangladesh' in line[0]:
            print(line)
            print(f'5000 BDT to USD is {float(line[2])*5000}')
            print(f'50 USD to BDT is {float(line[3])*50}')
