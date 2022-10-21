class PairElement:
    def __init__(self):
        self.indx = 1
        self.result = [-1, -1]

    def targetSum(self, l1, target):
        if l1[0]+l1[1] == target:
            self.result[0] = self.indx
            self.result[1] = self.indx+1
        else:
            if len(l1) > 2:
                self.indx += 1
                self.targetSum(l1[1:], target)
        return self.result


a = [10, 20, 10, 40, 50, 60, 70]
target = 50
result = PairElement().targetSum(a, target)
print(result[0], result[1])
