class SubSets:
    def sub(self, res, l1):
        if l1:
            return self.sub(res, l1[1:]) + self.sub(res + [l1[0]], l1[1:])
        return [res]


a = [4, 5, 6]
result = []
print(SubSets().sub(result, a))
