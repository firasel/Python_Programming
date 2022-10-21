s = input("enter string: ")
result = []
for i in range(0, len(s), 2):
    temp = ""
    for j in range(int(s[i+1])):
        temp += s[i]
    result.append(temp)
result = "".join(sorted(result, key=str.lower))
print("result is: ", result)
