import re

with open("sample.txt", "r") as f:
    data = f.read()
    # print(type(data))
    # pattern = re.compile(r"\d{10}")
    # pattern = re.compile(r"[0-9]{10}")
    # matches = pattern.finditer(data)
    split_data = data.splitlines()
    # print(split_data)
    print("-----------------------Passed students are------------------------------------")
    for item in split_data:
        # pattern = re.compile(r"^[0-9]{10}$")
        # pattern = re.compile(r"^[91]*[0-9]{10}$")
        # match = pattern.search(item)
        # if match:
        #     print(matches.group())
        pattern = re.compile(r"passed")
        match = pattern.search(item)
        if match:
            word = item.split()
            print(word[0])
    print("-----------------------Failed students are------------------------------------")
    for item in split_data:
        pattern_2 = re.compile(r"failed")
        match = pattern_2.search(item)
        if match:
            word = item.split()
            print(word[0])

