class Calculate:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def sum(self):
        return self.x+self.n

    def pow(self):
        res = 1
        for i in range(self.n):
            res *= self.x
        return res


calculator = Calculate(3, 3)
print(calculator.sum(), calculator.pow())
