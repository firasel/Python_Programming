import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('HR_comma_sep.csv')

# print(data.shape)

# Missing data
# print(data.isnull().values.any())

# Check data type
# print(data.dtypes)

# Check unique values
# print(data.salary.unique())
# print(data.Department.unique())

clean_up_values = {
    "salary": {
        "low": 1,
        "medium": 2,
        "high": 3,
    }
}

data.replace(clean_up_values, inplace=True)

# Get dummies for the department
dummies = pd.get_dummies(data.Department)
# print(dummies)

# Merge dummies (dummy columns) with the original data
merged = pd.concat([data, dummies], axis="columns")
# print(merged)

# Drop unnecessary columns
final_data = merged.drop(['Department', 'technical'], axis='columns')
# print(final_data.columns)

# Plot data set to see the data relation
# plt.scatter(x=final_data.time_spend_company, y=final_data.left)
# plt.show()

X = final_data.drop('left', axis='columns')
y = final_data.left

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(accuracy)
