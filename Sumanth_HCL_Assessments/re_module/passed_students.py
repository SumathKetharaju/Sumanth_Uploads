import re
students_with_result = {}

with open("all_data.txt", "r") as f:
    data = f.read()
    lines = data.splitlines()
    # print(lines)
    for line in lines:

        passed_pattern = re.compile(r"passed")
        failed_pattern = re.compile(r"failed")

        passed_match = passed_pattern.search(line)
        failed_match = failed_pattern.search(line)

        if passed_match:
            # print(passed_match)
            student = line.split()[0]
            # print(student)
            students_with_result[student.capitalize()] = passed_match.group().capitalize()

        if failed_match:
            # print(failed_match)
            student = line.split()[0]
            # print(student)
            students_with_result[student.capitalize()] = failed_match.group().capitalize()

print("----------------------------------------------------------------------------------------------------")
print(students_with_result)
print("----------------------------------------------------------------------------------------------------")

failed_students = []
passed_students = []

for key, value in students_with_result.items():
    if value == "Failed":
        failed_students.append(key)
    elif value == "Passed":
        passed_students.append(key)

print(f"Passed_students are --> {passed_students}")
print(f"Total number of Passed_students are --> {len(passed_students)}")
print("----------------------------------------------------------------------------------------------------")
print(f"failed_students are --> {failed_students}")
print(f"Total number of failed_students are --> {len(failed_students)}")


