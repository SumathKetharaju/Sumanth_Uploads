def student(name, college, branch):

    print(f"Here student name is {name}")
    print(f"He is studying {branch} engineering in {college}")
    return f"His college is located in nellore"


student("sumanth", "Gist", "civil")
print()

student("Gist", "sumanth", "civil")
print()

student(name="mahesh", college="Svcn", branch="Mechanical")
print()

sasi = student(branch="computer science", name="sasi",  college="Svcn")
print(sasi)
