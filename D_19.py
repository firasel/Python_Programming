""" All about mankind """


from xmlrpc.client import boolean


class Human:
    def __init__(self, gender, height, weight) -> None:
        self.gender = gender
        self.height = height
        self.weight = weight


class Police(Human):
    def __init__(self, gender, height, weight, cases, nationality) -> None:
        super().__init__(gender, height, weight)
        self.cases = cases
        self.nationality = nationality


class CsEngineer(Human):
    def __init__(self, gender, height, weight, love_to_code: boolean, has_gf: boolean) -> None:
        super().__init__(gender, height, weight)
        self.love_to_code = love_to_code
        self.has_gf = has_gf


police = Police('Male', 5.6, 56, False, 'BD')
print(police.__dict__)

eng = CsEngineer('Male', 5.8, 60, True, False)
print(eng.__dict__)
