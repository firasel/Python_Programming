class Student:
    def __init__(self, name, id, marks) -> None:
        self._name = name
        self.__id = id
        self.marks = marks

    @property
    def student_id(self):
        return self.__id

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name


rashid = Student('Rashid', 25, 60)

print(rashid.student_id)
print(rashid.name)
print(rashid.__dict__)
del rashid.name
print(rashid.__dict__)
