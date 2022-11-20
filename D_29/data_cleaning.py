import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv('iphone_price.csv')
plt.scatter(data['version'], data['price'])
plt.show()
