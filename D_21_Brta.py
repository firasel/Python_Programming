import random


class BRTA:
    def __init__(self) -> None:
        self.__license = {}

    def take_driving_test(self, email):
        self.email = email
        score = random.randint(0, 100)
        if score >= 33:
            # print("Congrats, you have passed")
            license_number = random.randint(4000, 9999)
            self.__license[email] = license_number
            return license_number
        else:
            # print("Sorry your failed")
            return False

    def validate_license(self, email, license):
        for key, val in self.__license.items():
            if key == email and val == license:
                return True
        return False
