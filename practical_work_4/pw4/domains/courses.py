import csv

def create_course(course_file, information):
    f = open(course_file, "a")
    writer =  csv.writer(f)
    writer.writerow(information)
    f.close()
