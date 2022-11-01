import hashlib
from pdb import line_prefix
from random import randint

from D_21_Brta import BRTA
from D_21_RideManager import uber
from D_21_Vehicles import Bike, Car, Cng

license_authority = BRTA()


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        with open('users.txt', 'r+') as file:
            flag = True
            line = file.readlines()
            for item in line:
                if item.split(' ')[0] == email:
                    flag = False
                    item.replace(
                        item, f'{email} {pwd_encrypted}\n')
            if flag:
                file.write(f'{email} {pwd_encrypted}\n')
        file.close()
        # print(self.name, "User created")

    @staticmethod
    def log_in(email, password):
        stored_password = ""
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    _, stored_password = line.split(' ')
        file.close()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == stored_password:
            return True
        else:
            return False


class Rider(User):
    def __init__(self, name, email, password, location, balance) -> None:
        self.location = location
        self.balance = balance
        self.__trip_history = []
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self, destination):
        pass

    def get_trip_history(self):
        return self.__trip_history

    def start_a_trip(self, fare, trip_info):
        self.balance -= fare
        self.__trip_history.append(trip_info)

    pass


class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        super().__init__(name, email, password)
        self.location = location
        self.__trip_history = []
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0

    def take_driving_test(self):
        result = license_authority.take_driving_test(self.email)
        if result == False:
            # print("Sorry you failed, try again")
            self.license = None
        else:
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver is True:
            if vehicle_type == 'car':
                new_vehicle = Car(
                    vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle('car', new_vehicle)
            elif vehicle_type == 'bike':
                new_vehicle = Bike(
                    vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle('bike', new_vehicle)
            else:
                new_vehicle = Cng(
                    vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle('cng', new_vehicle)
        else:
            pass
            # print("You are not a valid driver")

    def get_trip_history(self):
        return self.__trip_history

    def start_a_trip(self, destination, fare, trip_info):
        self.earning += fare
        self.location = destination
        self.__trip_history.append(trip_info)


rider1 = Rider('rider1', 'rider1@gmail.com', 'rider1', randint(0, 30), 1000)
rider2 = Rider('rider2', 'rider2@gmail.com', 'rider2', randint(0, 30), 5000)
rider3 = Rider('rider3', 'rider3@gmail.com', 'rider3', randint(0, 30), 5000)

for i in range(1, 100):
    driver1 = Driver(f'driver{i}', f'driver{i}@gmail.com',
                     f'driver{i}', randint(0, 100), randint(1000, 9999))
    driver1.take_driving_test()
    driver1.register_a_vehicle('car', randint(10000, 99999), 10)


uber.find_a_vehicle(rider1, 'car', randint(1, 100))
uber.find_a_vehicle(rider1, 'car', randint(1, 100))
uber.find_a_vehicle(rider1, 'car', randint(1, 100))
uber.find_a_vehicle(rider1, 'car', randint(1, 100))

print(rider1.get_trip_history())
