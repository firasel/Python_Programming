# Multiple inheritance
class School:
    def __init__(self, school_name) -> None:
        self.school_name = school_name
        print("School init called")


class Grade:
    def __init__(self, grade_name) -> None:
        self.grade_name = grade_name
        print("Grade class init called")


class Student(School, Grade):
    def __init__(self, name, grade_name, school_name) -> None:
        self.name = name
        print("Student init called")
        School.__init__(self, school_name)
        Grade.__init__(self, grade_name)


david = Student('David', 'BSC', 'AB School')
print(david.__dict__)
