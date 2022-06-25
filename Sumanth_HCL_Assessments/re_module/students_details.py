import re
# passed_students_with_years = {"Sumanth":[1st, 3rd]}
passed_students_with_years = {}
first_years = []
second_years = []

with open("all_data.txt", "r") as f:
    data = f.read()
    lines = data.splitlines()
    # print(lines)
    for line in lines:
        first_year_pattern = re.compile(r"1st")
        second_year_pattern = re.compile(r"2nd")
        passed_pattern = re.compile(r"passed")
        failed_pattern = re.compile(r"failed")
        first_year_match = first_year_pattern.search(line)
        second_year_match = second_year_pattern.search(line)
        passed_match = passed_pattern.search(line)
        failed_match = failed_pattern.search(line)
        if first_year_match:
            if passed_match:
                print(passed_match)
                # # print(first_year_match)
                first_year = first_year_match.group()
                student = line.split()[0]
                print(student)
                first_years.append(first_year)
                # print(first_years)
                passed_students_with_years[student] = first_years
                # first_years = first_years[:]

            # print(first_year_match)
        if second_year_match:
            if passed_match:
                # print(second_year_match)
                second_year = second_year_match.group()
                student = line.split()[0]
                print(student)
                second_years.append(second_year)
                # duplicate_2 = duplicate[:]
                passed_students_with_years[student] = second_years
                # print(first_year_match)
print(passed_students_with_years)

