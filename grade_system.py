student_name=input("Enter the student name: ")
student = {
    "Abel": 85,
    "Mikiyas": 92,
    "Sara": 78,
    "Liya": 88,
    "Noah": 90}
def get_grade(student,student_name):
    try:
        return student[student_name]
    except KeyError:
        return "Student not found"
print(get_grade(student, student_name))

    


    

