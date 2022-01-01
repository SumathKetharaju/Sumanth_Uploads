# iam24sumanth3working45developer
import re
input_string = "iam24sumanth3working45developer"

pattern = re.compile("\d+")

result = pattern.findall(input_string)

print(result)
count = 0
for item in result:
    count += int(item)

print(count)



