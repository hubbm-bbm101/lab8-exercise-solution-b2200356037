import sys

records = sys.argv[1]
student_names = sys.argv[2]

with open(records, encoding="utf-8") as student_content:
    student_list = []
    for student in student_content.readlines():
        student = student.split(":")
        student[1] = student[1].strip("\n")
        student_list.append(student)

student_dict = {student: university for student, university in student_list}
student_names = student_names.split(",")

for name in student_names:
    try:
        assert name in student_dict
        print("Name: %s, University: %s" % (name, student_dict[name]))
    except:
        print("No record of '%s' was found!" % name)