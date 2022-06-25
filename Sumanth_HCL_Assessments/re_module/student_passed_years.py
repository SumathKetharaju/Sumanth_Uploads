import re

first_year_passed_students = []
second_year_passed_students = []
person_1_passed_years = []
person_2_passed_years = []
person_3_passed_years = []
person_4_passed_years = []

student_dict = {}

with open("btech_passedout_students_list.txt", "r") as f:
    data = f.read()
    # print(data)
    lines = data.splitlines()
    # print(lines)
    for line in lines:
        passed_pattern = re.compile(r".* passed .*")
        passed_match = passed_pattern.search(line)
        first_year_pattern = re.compile(r"1st")
        second_year_pattern = re.compile(r"2nd")
        first_year_match = first_year_pattern.search(line)
        second_year_match = second_year_pattern.search(line)
        if passed_match:
            if first_year_match:
                print(passed_match)
                student = line.split()[0]
                first_year = first_year_match.group()
                first_year_passed_students.append(student)
                # second_year = second_year_match.group()
                # second_year_passed_students.append(student)
                if student in first_year_passed_students[0]:
                    person_1_passed_years.append(first_year)
                    # person_1_passed_years.append(second_year)
                    student_dict[student] = person_1_passed_years
                elif student in first_year_passed_students[1]:
                    person_2_passed_years.append(first_year)
                    # person_2_passed_years.append(second_year)
                    student_dict[student] = person_2_passed_years
            elif second_year_match:
                print(passed_match)
                student = line.split()[0]
                second_year = second_year_match.group()
                second_year_passed_students.append(student)
                if student in second_year_passed_students[0]:
                    person_1_passed_years.append(second_year)
                    student_dict[student] = person_1_passed_years
                elif student in second_year_passed_students[1]:
                    person_2_passed_years.append(second_year)
                    student_dict[student] = person_2_passed_years


print(person_1_passed_years)
print(person_2_passed_years)
print(first_year_passed_students)
print(second_year_passed_students)
print(student_dict)
