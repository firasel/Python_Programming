import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
from sklearn.model_selection import train_test_split

digits = load_digits()

# print(digits.data.shape)
# print(dir(digits))

# plt.gray()
# plt.matshow(digits.images[0])
# plt.show()

X = digits.data
Y = digits.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# print(X_train.shape)
# print(X_test.shape)

model = LogisticRegression()
model.fit(X_train, Y_train)

# print(digits.target[1700])
# result = model.predict([digits.data[1700]])
# print(result)

accuracy = model.score(X_test, Y_test)
# print(accuracy)

Y_predicted = model.predict(X_test)
confusion = confusion_matrix(Y_test, Y_predicted)

plot_confusion_matrix(model, X_test, Y_test)
plt.show()
