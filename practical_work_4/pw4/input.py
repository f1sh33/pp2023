def student_number():
    number = int(input("Enter number of student: "))
    return number

def course_number():
    number = int(input("Enter number of course: "))
    return number

def student():
    id = input("Enter Student's ID: ")
    name = input("Enter Student's Name: ")
    dob = input("Enter Student's Date of Birth: ")
    return [id, name, dob]

def course():
    id = input("Enter Couse ID: ")
    name = input("Enter Course Name: ")
    credit = int(input("Enter Course Credit: "))
    return [id, name, credit]

def mark(student_id, course_name):
    mark = int(input(f"Enter the mark of student {student_id} on the course {course_name}: "))
    return(mark);