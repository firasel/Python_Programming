# Problem 1
# str1 = 'pHitrOn.iO presents "Python COuRSe"'
# print(str1)
# result = ""
# for letter in str1:
#     if letter >= 'A' and letter <= 'Z':
#         result += chr(ord(letter)+32)
#     elif letter >= 'a' and letter <= 'z':
#         result += chr(ord(letter)-32)
#     else:
#         result += letter
# print(result)


# Problem 2
# n = input("Enter a number: ")
# for i in range(1, int(n)+1):
#     for j in range(1, i+1):
#         print(f'{j} ', end="")
#     print()

# print()
# # Using one for loop
# str = ""
# for i in range(1, int(n)+1):
#     str += f'{i} '
#     print(str)


# Problem 3
# n = int(input("Enter a number for terms: "))
# prev = 0
# curr = 1
# if n > 0:
#     print(prev, end=" ")
# if n > 1:
#     print(curr, end=" ")
# for i in range(n-2):
#     temp = prev + curr
#     prev = curr
#     curr = temp
#     print(temp, end=" ")


# Problem 4
# str1 = "P@#yn26at^&i5ve"
# upCase = 0
# lwCase = 0
# digits = 0
# symbols = 0

# for letter in str1:
#     if letter >= 'A' and letter <= 'Z':
#         upCase += 1
#     elif letter >= 'a' and letter <= 'z':
#         lwCase += 1
#     elif letter >= '0' and letter <= '9':
#         digits += 1
#     else:
#         symbols += 1

# print(
#     f'UpperCase = {upCase}\nLowerCase = {lwCase}\nDigits = {digits}\nSymbol = {symbols}')


# Problem 5
# str1 = "Abc"
# str2 = "Xyz"
# res = ""
# minSize = min(len(str1), len(str2))
# for i in range(minSize):
#     res += str1[i] + str2[minSize-i-1]
# print(res)


# Problem 6
# str1 = "Phi"
# str2 = "Phitron"
# res = True
# minSize = min(len(str1), len(str2))
# for i in range(len(str1)):
#     chk = True
#     for j in range(len(str2)):
#         if str1[i] == str2[j]:
#             chk = False
#     if chk:
#         res = False
# print(res)


# Problem 7
# num = int(input("Enter a number: "))
# num1 = num
# num2 = 0
# while num1 > 0:
#     num2 = int((num2*10)+(num1 % 10))
#     num1 = int(num1/10)
# print(num2 == num)


# Problem 8
# num1 = int(input("Enter the start number: "))
# num2 = int(input("Enter the end number: "))
# if num1 == 0 or num1 == 1:
#     num1 = 2
# if num1 % 2 == 0:
#     if (num1 == 2):
#         print("2 ")
#     num1 += 1

# for i in range(num1, num2, 2):
#     chk = True
#     for j in range(2, i):
#         if i % j == 0:
#             chk = False
#             break
#     if chk:
#         print(i)


# Problem 9
num1 = int(input("Enter a number: "))
num2 = 0
while num1 > 0:
    num2 = int((num2*10)+(num1 % 10))
    num1 = int(num1/10)
print(num2)
