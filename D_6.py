# Function Practice
# Add two number
def addTwo(num1, num2):
    print(f'Num1 = {num1}, Num2 = {num2}')
    return num1+num2


result = addTwo(10, 26)
print(result)
result = addTwo(num2=20, num1=15)
print(result)

# Double a number


def double_it(num1):
    return num1*2


result = double_it(49)
print(result)

# Multiple arguments


def addNums(*nums):
    result = 0
    for num in nums:
        result += num
    return result


result = addNums(1, 2, 3, 4, 5)
print(result)
