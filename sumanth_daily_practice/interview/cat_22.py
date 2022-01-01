import re
# sumath.ketharju@gmail.com
# inp1 = 1hello@mail.com
# inp2= Hello1@mail.com
# inp3 = hello#$@.com
# inp4 = hello~@mail.com
# inp5 = hello@mail.world
# inp6= hello_world@mail.com
email_address = input("Enter an Email address:")
# pattern_1 = re.compile(r"^[a-z](\.|\-)?[a-z][@]+[a-z][.][a-z]{3}")
pattern = re.compile(r'\b[A-Za-z._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

match = pattern.search(email_address)

if match:
    print("It is valid email address")
else:
    print("It is not valid email address")
