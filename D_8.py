# Practice problem 1
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
