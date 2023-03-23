import input
import csv
import numpy as np

def clear_data(file_names):
    for file in file_names:
        with open(file, 'w') as f:
            f.write("");

def list_courses(course_file):
    c = open(course_file, "r")
    c_read = csv.reader(c)
    for course in c_read:
        print(f"Course: {course[1]} --- ID: {course[0]} --- Credit: {course[2]}")
    c.close()
        

def list_student(student_file):
    s = open(student_file)
    s_read = csv.reader(s)
    for student in s_read:
        print(f"Student: {student[1]} --- ID: {student[0]} --- Dob: {student[2]}")

def input_mark(student_file, course_file, mark_file):
    c = open(course_file, "r")
    s = open(student_file, "r")
    m = open(mark_file, "w")
    c_read = csv.reader(c)
    s_read = csv.reader(s)
    m_write = csv.writer(m)
    all_course = [row[1] for row in c_read]
    all_student = [row[0] for row in s_read]
    for course in all_course:
        mark = []
        for student in all_student:
            input_mark = input.mark(student, course)
            mark.append(input_mark)
        m_write.writerow(mark)
    c.close()
    s.close()
    m.close()

def calculate_gpa(student_file, course_file, mark_file):
    s = open(student_file, "r")
    c = open(course_file, "r")
    s_read = csv.reader(s)
    c_read = csv.reader(c)
    all_credit = [int(row[2]) for row in c_read]
    for i, student in enumerate(s_read):
        m = open(mark_file, "r")
        m_read = csv.reader(m)
        all_mark = [int(row[i]) for row in m_read]
        weighted_sum = np.array(all_mark) * np.array(all_credit)
        total_weighted_sum = np.sum(weighted_sum)
        total_credit = np.sum(all_credit)
        gpa = np.round(total_weighted_sum/total_credit, decimals=1)
        print(f"GPA for the student {student[0]} is {gpa}.")
        m.close()

    s.close()
    c.close()