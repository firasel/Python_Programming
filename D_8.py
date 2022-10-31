# Practice problem 1
from audioop import reverse


def show_employee(name="Anonymous", salary=9000):
    print(f'Name: {name}, Salary: {salary}')


show_employee("Md Rakib", 5000)
# Practice problem 2


def calculation(a, b):
    return {"addition": a+b, "subtraction": a-b}


result = calculation(20, 5)
print(f'Addition: {result["addition"]}, Subtraction: {result["subtraction"]}')
# Practice problem 3
list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd"]
result = [word+list2[i] for i, word in enumerate(list1)]
print(result)
# Practice problem 4
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
result = zip(list1, reversed(list2))
for num1, num2 in result:
    print(num1, num2)
# Practice problem 5
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)
# Practice problem 6
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
result = {key: value for key, value in sample_dict.items()
          for targetKey in keys if targetKey == key}
print(result)
# Practice problem 7
sample_dict = {'a': 100, 'b': 200, 'c': 300}
result = False
for num in sample_dict.values():
    if num == 100:
        result = True
        break
if result:
    print("Present")
else:
    print("Not Present")
# Practice problem 8
tuple1 = (11, [22, 33], 44, 55)
for value in tuple1:
    if type(value) == list:
        lastNum = value[0] % 10
        value[0] = value[0]*10+lastNum
print(tuple1)
# Practice problem 9
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))
# Practice problem 10
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)
