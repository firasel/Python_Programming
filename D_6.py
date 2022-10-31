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

# Arguments


def wordsPrint(word1, *words, **allWord):
    print(word1)
    for word in words:
        print(word, end=" ")
    print()
    for key, value in allWord.items():
        print(key, value)


wordsPrint("Word 1", "Word 2", "Word 3", "Word 4",
           word5="Word 5", word6="Word 6", word7="Word 7")

# Golbal variable edit
balance = 260


def total_cost(price, quantity):
    global balance
    balance = balance-(price*quantity)


print(f'Balance before: {balance}')
total_cost(10, 3)
print(f'Balance after: {balance}')
