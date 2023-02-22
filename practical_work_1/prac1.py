classStudent = []
courses = []

def construct_student(id, name, dob):
    data = {
        "id": id,
        "name": name,
        "dob": dob,
        "classes": []
    }
    return data

def construct_course(id, name):
    data = {
        "id": id,
        "name": name
    }
    return data

def find_course(id, courses):
    for course in courses:
        if course["id"] == id:
            return course
    return 0

def list_course(courses):
    print("All Courses Information: ")
    print("------------------------")
    for course in courses:
        print("ID: " + course["id"])
        print("Name: " + course["name"])
    print("------------------------")
    print("")

def list_student(students):
    print("All Student Information: ")
    print("------------------------")
    for student in students:
        print("ID: " + student["id"])
        print("Name:" + student["name"])
        print("DoB: " + student["dob"])
        print("")
    print("------------------------")
    print("")

def list_mark(students, courseId):
    course = find_course(courseId, courses)
    courseName = course["name"]
    print(f"Mark Information for course {courseId} - {courseName}:")
    for student in students:
        for attendedClass in student["classes"]:
            if (attendedClass["id"] == courseId):
                print(student["name"] + ": " + attendedClass["mark"])


# Get input data for all Students

studentNumber = int(input("Enter the number of students: "))

for student in range(0, studentNumber):
    id = input(f"Enter ID of the {student+1} student: ")
    name = input(f"Enter Name of the {student+1} student: ")
    dob = input(f"Enter DoB of the {student+1} student: ")
    print("")
    classStudent.append(construct_student(id, name, dob));

# Get input data for all Courses

courseNumber = int(input("Enter the number of courses: "))

for course in range(0, courseNumber):
    id = input(f"Enter ID of the {course+1} course: ")
    name = input(f"Enter name of the {course+1} course: ")
    print("")
    courses.append(construct_course(id, name))  

for i in range(0, courseNumber):
    while (True):
        desiredCourseId = input("Enter the ID of the course you want to input marks: ")
        if (find_course(desiredCourseId, courses)):
            break
        else:
            print("The course you entered is not available! Please enter another name...")
    
    for student in classStudent:
        name = student["name"]
        student_mark = input(f"Enter {name}'s mark for {desiredCourseId} course: ")
        data = {
            "id": desiredCourseId,
            "mark": student_mark
        }
        student["classes"].append(data);


list_course(courses)
list_student(classStudent)
while (True):
    courseId = input("Enter the ID of the course you want to list mark: ")
    if (not find_course(courseId, courses)):
        print("The course you entered is not available! Please enter another name...")
        continue
    list_mark(classStudent, courseId)