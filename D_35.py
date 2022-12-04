# Single Inheritance
# When a child class inherits from only one parent class, it is called single inheritance.
class Parent:
    def __init__(self) -> None:
        print("Parent class")


class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        print("Child class")


Child()

# Multiple inheritances
# When a child class inherits from multiple parent classes, it is called multiple inheritances.


class Parent1:
    def __init__(self) -> None:
        print("Parent1 class")


class Parent2:
    def __init__(self) -> None:
        print("Parent2 class")


class Child(Parent1, Parent2):
    def __init__(self) -> None:
        Parent1.__init__(self)
        Parent2.__init__(self)
        print("Child class")


Child()

# Multilevel inheritance
# Multi-level inheritance is archived when a derived class inherits another derived class.


class Parent:
    def __init__(self) -> None:
        print("Parent class")


class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        print("Child class")


class GrandChild(Child):
    def __init__(self) -> None:
        super().__init__()
        print("GrandChild class")


GrandChild()
