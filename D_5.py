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
n = input("Enter a number: ")
for i in range(1, int(n)+1):
    for j in range(1, i+1):
        print(f'{j} ', end="")
    print()

print()
# Using one for loop
str = ""
for i in range(1, int(n)+1):
    str += f'{i} '
    print(str)
