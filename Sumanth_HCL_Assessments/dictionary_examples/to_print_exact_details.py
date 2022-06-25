empty_dict = {}

a_grade_students = []
b_grade_students = []
c_grade_students = []

students_with_grades = {'Sasi': 'A', 'Suresh': 'C', 'Ravi': 'B', 'Sumanth': 'C', 'Praveen': 'A', "Jafrulla": "B"}

for name, grade in students_with_grades.items():
    if grade == "A":
        a_grade_students.append(name)
    elif grade == "B":
        b_grade_students.append(name)
    else:
        c_grade_students.append(name)

print(a_grade_students)
print(b_grade_students)
print(c_grade_students)




# grades
# {'Ashley': 'A', 'Betty': 'B', 'Emily': 'A+', 'John': 'A', 'Mike': 'C'}


