def faculty(name, age=30, subject="surveying", lab="SM"):

    print(f"The faculty name is {name} and his age is {age}")
    print(f"He will be teaching {subject} subject")
    return f"He helps to students {lab} laboratory"


faculty("Anil")
print()

faculty("Anil", 31, "SM", 5)
print()

print(faculty("Anil", 32, lab="FM"))
