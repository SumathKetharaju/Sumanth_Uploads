import re

python_resources = {}
java_resources = {}
embeddedc_resources = {}

with open("employees_details.txt", "r") as f:
    data = f.read()
    # print(data)
    lines = data.splitlines()
    # print(lines)
    print(len(lines))
    for line in lines:

        python_pattern = re.compile(r".* in Python")
        java_pattern = re.compile(r".* in Java")
        embeddedc_pattern = re.compile(r".* in Embeddedc")
        employee_pattern = re.compile(r".* is")
        years_pattern = re.compile(r"having .* years")
        python_match = python_pattern.search(line)
        java_match = java_pattern.search(line)
        embeddedc_match = embeddedc_pattern.search(line)
        years_match = years_pattern.search(line)
        employee_match = employee_pattern.search(line)
        if python_match:
            # print(python_match.group())
            # print(years_match.group())
            # print(employee_match.group())
            python_employee = employee_match.group()[:-3]
            python_employee_year = years_match.group()[7:-6]
            # print(python_employee)
            # print(python_employee_year)
            python_resources[python_employee.capitalize()] = python_employee_year
        elif java_match:
            # print(java_match.group())
            # print(years_match.group())
            # print(employee_match.group())
            java_employee = employee_match.group()[:-3]
            java_employee_year = years_match.group()[7:-6]
            # print(java_employee)
            # print(java_employee_year)
            java_resources[java_employee.capitalize()] = java_employee_year
        else:
            # print(embeddedc_match.group())
            # print(years_match.group())
            # print(employee_match.group())
            embeddedc_employee = employee_match.group()[:-3]
            embeddedc_employee_year = years_match.group()[7:-6]
            # print(java_employee)
            # print(java_employee_year)
            embeddedc_resources[embeddedc_employee.capitalize()] = embeddedc_employee_year


print(f"Python Resources are --> {python_resources}")
print(f"Java Resources are --> {java_resources}")
print(f"Embeddedc Resources are --> {embeddedc_resources}")
# print(java_resources)
# print(embeddedc_resources)
