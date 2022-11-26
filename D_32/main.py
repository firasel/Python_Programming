def sum_odd(n):
    total = 0
    if (n % 2 == 0):
        n -= 1
    for i in range(3, n+1, 2):
        total += i
    return total


print(sum_odd(10))
print(sum_odd(5))
