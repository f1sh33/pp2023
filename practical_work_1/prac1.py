classStudent = []
courses = []

# Construct a Student dict to push to a ClassStudent list
def constructStudent(id, name, dob):
    data = {
        "id": id,
        "name": name,
        "dob": dob,
        "classes": []
    }
    return data

# Construct a Course dict to push to a Courses list
def constructCourse(id, name):
    data = {
        "id": id,
        "name": name
    }
    return data

# Find a course based on a passed ID
def findCourse(id, courses):
    for course in courses:
        if course["id"] == id:
            return course
    return 0

# List all Courses
def listCourse(courses):
    print("All Courses Information: ")
    print("------------------------")
    for course in courses:
        print("ID: " + course["id"])
        print("Name: " + course["name"])
    print("------------------------")
    print("")

# List all Students
def listStudent(students):
    print("All Student Information: ")
    print("------------------------")
    for student in students:
        print("ID: " + student["id"])
        print("Name:" + student["name"])
        print("DoB: " + student["dob"])
        print("")
    print("------------------------")
    print("")

# List mark of students based on passed Course ID
def listMark(students, courseId):
    course = findCourse(courseId, courses)
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
    classStudent.append(constructStudent(id, name, dob));

# Get input data for all Courses

courseNumber = int(input("Enter the number of courses: "))

for course in range(0, courseNumber):
    id = input(f"Enter ID of the {course+1} course: ")
    name = input(f"Enter name of the {course+1} course: ")
    print("")
    courses.append(constructCourse(id, name))  

# Select course for mark inputting
for i in range(0, courseNumber):
    while (True):
        desiredCourseId = input("Enter the ID of the course you want to input marks: ")
        if (findCourse(desiredCourseId, courses)):
            break
        else:
            print("The course you entered is not available! Please enter another name...")
    
    for student in classStudent:
        name = student["name"]
        studentMark = input(f"Enter {name}'s mark for {desiredCourseId} course: ")
        data = {
            "id": desiredCourseId,
            "mark": studentMark
        }
        student["classes"].append(data);

listCourse(courses)
listStudent(classStudent)

while (True):
    courseId = input("Enter the ID of the course you want to list mark: ")
    if (not findCourse(courseId, courses)):
        print("The course you entered is not available! Please enter another name...")
        continue
    listMark(classStudent, courseId)