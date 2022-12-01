import json
import math

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("./datasets/salary.csv")
headers = data.columns.values

X = data[headers[0]]
Y = data[headers[1]]

X = X.truncate(4900, 4999)
Y = Y.truncate(4900, 4999)

with open("./trained/trained_data.txt") as file:
    data = file.read()
    converted = json.loads(data)

m = converted["m"]
c = converted["c"]
Y_predicted_list = []

for val in X:
    Y_predicted = (m*val)+c
    Y_predicted_list.append(Y_predicted)

plt.scatter(X, Y, color="g")
plt.plot(X, Y_predicted_list, color="r")
plt.show()
