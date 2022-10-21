import math


class Distance:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate(self):
        return math.sqrt(math.pow(self.x2-self.x1, 2)+math.pow(self.y2-self.y1, 2)*1.0)


x1 = 3
y1 = 4
x2 = 7
y2 = 8
calculator = Distance(x1, y1, x2, y2)
print("%.2f" % calculator.calculate())
