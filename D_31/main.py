import matplotlib.pyplot as plt
import pandas as pd

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
print(final_data.columns)
plt.scatter(x=final_data.time_spend_company, y=final_data.left)
plt.show()
