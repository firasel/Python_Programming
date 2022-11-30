from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):
    def go(self):
        print("Car started")


class Bike(Vehicle):
    def go(self):
        print("Bike started")


car = Car()
car.go()
bike = Bike()
bike.go()
