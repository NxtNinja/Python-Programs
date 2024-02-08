def highest_marks_students(students):
    highest_marks = 0
    highest_student = ""

    for student, marks in students.items():
        if marks > highest_marks:
            highest_marks = marks
            highest_student  = student

    return highest_marks, highest_student


students_registry = {}

num_students = int(input("Enter no. of students: "))

for _ in range(num_students):
    name = input("Enter student name: ")
    marks = float(input("Enter marks for {}: ".format(name)))
    students_registry[name] = marks

#print(students_registry)
marks , student = highest_marks_students(students_registry)

print(student,"is the highest with",marks,"marks")
