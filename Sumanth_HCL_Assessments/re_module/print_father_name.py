import re

family_dict = {}

with open("family_list.txt", "r") as f:
    data = f.read()
    # print(data)
    lines = data.splitlines()
    # print(lines)
    for line in lines:
        father_pattern = re.compile(r"of .+ and")
        son_pattern = re.compile(r".+ is")
        father_match = father_pattern.search(line)
        son_match = son_pattern.search(line)
        if father_match:
            father_name = father_match.group()[3:-4]
            # print(father_name)
            son_name = son_match.group()[:-3]
            # print(father_name)
            # print(son_name)
            family_dict[father_name.upper()] = son_name.capitalize()

print(family_dict)



