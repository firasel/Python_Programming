def mylen(l):
    ans = 0
    for i in l:
        ans += 1
    return ans


print(mylen([1, 4, 2, 3, 5]))
print(mylen([2, 3, 8, 9, 0, 1, 3]))
print(mylen([]))
