sample_dict = {"Sumanth": 1.5, "mahesh": 1.5, "Ramesh": 2.2}

one_plus_year_students = []

for key, value in sample_dict.items():
    if 1 < value < 2:
        one_plus_year_students.append(key)
    # elif if 1 < value < 2

print(one_plus_year_students)


