print("Enter a blank student name and the program will end.")
while True:
    student_name = input("\nStudent Name: ")
    if student_name == "":
        break
    mark = int(input("Mark: "))
    f = open('studentData.txt', 'r+')
    student_id = len(f.readlines())+1
    f.write(f'Id: {student_id}, Name: {student_name}, Mark: {mark}\n')
    f.close()
