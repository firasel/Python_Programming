class Person:
    count = 0

    def __init__(self) -> None:
        Person.count += 1


person1 = Person()
person2 = Person()
person3 = Person()

print(Person.count)


def parent(func):
    print("Parent Called")
    return func


@parent
def child():
    print("Child Called")


child()
