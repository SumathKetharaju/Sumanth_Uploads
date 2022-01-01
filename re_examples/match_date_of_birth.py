import re
# input_date_of_birth = "11-12-1998" #pass
# input_date_of_birth = "36/6/1998" #it should fail
# input_date_of_birth = "0-1-2022" #it should fail
# input_date_of_birth = "11/6/1998" #pass
# input_date_of_birth = "11/0/1998" #it should fail
# input_date_of_birth = "11/88/1998" #it should fail
# input_date_of_birth = "11@06@1998" #it should fail
# input_date_of_birth = "1-1-2022" #pass
input_date_of_birth = "1-1-1" #pass

# input_email = input("Enter email: ")

# pattern = re.compile(r"^[1-9]|1[0-9]|2[0-9]|3[0-1][-]+[0-9]|1[0-2][-]+\d{4}$")
# pattern = re.compile(r"^([1-9]|1[0-9]|2[0-9]|3[0-1])+(\-|\/)+([0-9]|1[0-2])+(\-|\/)+\d{4}$")  #correct
pattern = re.compile(r"(^[1-9]|1[0-9]|2[0-9]|3[0-1])+(\-|\/)+(\b[1-9]|1[0-2])+(\-|\/)+\d+$")  #Exactly correct


match = pattern.search(input_date_of_birth)

print(match)

if match:
    print("Valid date of birth")
else:
    print("Not a valid date of birth")