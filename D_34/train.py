import json
import math

import pandas as pd


def calculate_mean(data):
    sum = 0
    for val in data:
        sum += val
    return sum/len(data)


data = pd.read_csv('./datasets/salary.csv')
headers = data.columns.values
X = data[headers[0]]
Y = data[headers[1]]

X = X.truncate(0, 4899)
Y = Y.truncate(0, 4899)

X_mean = calculate_mean(X)
Y_mean = calculate_mean(Y)

upper = 0
lower = 0
for indx in range(len(X)):
    upper += (X[indx]-X_mean)*(Y[indx]-Y_mean)
    lower += math.pow(X[indx]-X_mean, 2)

m = upper/lower
c = Y_mean-(m*X_mean)
with open("./trained/trained_data.txt", 'w') as file:
    file.write(json.dumps({"m": m, "c": c, "Y_mean": Y_mean}))
file.close()
