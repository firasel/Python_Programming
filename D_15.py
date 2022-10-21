totalStudent = int(input("Enter the total student number: "))
while totalStudent:
    student_name = input("Student Name: ")
    mark = int(input("Mark: "))
    file = open('studentData.txt', 'r+')
    student_id = len(file.readlines())+1
    file.write(f'Id: {student_id}, Name: {student_name}, Mark: {mark}\n')
    file.close()
    totalStudent -= 1
