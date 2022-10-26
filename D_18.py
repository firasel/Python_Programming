class Person:
    count = 0

    def __init__(self) -> None:
        Person.count += 1


person1 = Person()
person2 = Person()
person3 = Person()

print(Person.count)
