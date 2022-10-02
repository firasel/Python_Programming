from math import ceil, floor

# Practice Problem 1
num = float(input("Enter a floating number: "))
print(f'Floor is {floor(num)} and Ceil is {ceil(num)}')

# Practice Problem 2
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
if num1 < 0:
    num1 = (-num1)
if num2 < 0:
    num2 = (-num2)
if num3 < 0:
    num3 = (-num3)

print(f'Num1: {num1}\nNum2: {num2}\nNum3: {num3}')
