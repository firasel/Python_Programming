class Vehicle:
    testScore = []

    def __init__(self, name, mileage, capacity, model, update):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
        self._model = model
        self.__update = update

    def __str__(self) -> str:
        return f'Name: {self.name}, Mileage: {self.mileage}, Capacity: {self.capacity}, Model: {self._model}, Update: {self.__update}'

    @property
    def vehicleMileage(self):
        return self.mileage

    @vehicleMileage.setter
    def vehicleMileage(self, newMileage):
        self.mileage = newMileage


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50, 2018, 2019)
# Question 2
print(type(School_bus))
# Question 3
print(isinstance(School_bus, Vehicle))
# Question 4
School_bus.testScore.extend([10, 20])
Personal_bus = Bus("Personal Bus", 20, 60, 2019, 2021)
print(School_bus.testScore, Personal_bus.testScore)
Personal_bus.testScore.extend([30, 40])
print(School_bus.testScore, Personal_bus.testScore)
# Question 5
print(School_bus.vehicleMileage)
School_bus.vehicleMileage = 15
print(School_bus.vehicleMileage)
# Question 6
print(School_bus)
print(Personal_bus)
# Question 8
print(School_bus._model)
# print(School_bus.__update)
