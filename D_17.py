from abc import ABC, abstractmethod


# Abstract base class
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    def name(self):
        pass

    def move(self):
        print("moving around in the zoo")


class Monkey(Animal):
    def sing(self):
        print('monkey is signing')

    def eat(Self):
        print("eating banana")


lyka = Monkey()
print(lyka)
lyka.eat()
lyka.move()
