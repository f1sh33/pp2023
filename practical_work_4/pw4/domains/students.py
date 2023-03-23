import csv

def create_student(student_file, information):
    f = open(student_file, "a")
    writer =  csv.writer(f)
    writer.writerow(information)
    f.close()