import re
input_email = "sumanth.ketharaju243@gmail.com" #Valid Email
# input_email = "1hello@gmail.com" #Not a Valid Email
# input_email = "Hello1@gmail.com" #Valid Email
# input_email = "hello#$@.com" #Not a Valid Email
# input_email = "hello~@gmail.com" #Not a Valid Email
# input_email = "hello@gmail.world" #Not a Valid Email
# input_email = "hello_world@gmail.com" #Valid Email


pattern = re.compile(r"^[a-zA-Z]+(\.|-|_)?[\w]*[@]+[a-z]{5}[\.]+[a-z]{3}$")

match = pattern.search(input_email)

if match:
    print("Valid Email")
else:
    print("Not a Valid Email")


