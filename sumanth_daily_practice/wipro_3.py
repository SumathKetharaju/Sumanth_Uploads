import re

input_string = "hello world hello"

pattern = "hello/b"

result = re.match(pattern, input_string)

if result:
    print("Success")
else:
    print("Not success")
