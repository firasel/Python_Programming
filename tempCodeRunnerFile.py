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