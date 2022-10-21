def exp(a, n):
    res = 1
    for i in range(n):
        res *= a
    return res


a, n = [int(num) for num in input("enter numbers: ").split()]
print("result is:", exp(a, n))
