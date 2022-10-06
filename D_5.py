str1 = 'pHitrOn.iO presents "Python COuRSe"'
print(str1)
result = ""
for letter in str1:
    if letter >= 'A' and letter <= 'Z':
        result += chr(ord(letter)+32)
    elif letter >= 'a' and letter <= 'z':
        result += chr(ord(letter)-32)
    else:
        result += letter
print(result)
