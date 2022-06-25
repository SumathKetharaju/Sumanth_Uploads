# to find how many a are there in my name --> sumanthketharaju
import re


class FindA:

    def __init__(self, name, char):
        self.name = name
        self.char = char

    def count_char(self):
        a_pattern_match = re.findall(self.char, self.name)
        print(f"count of {self.char} in my name {self.name} is --> {len(a_pattern_match)}")


find_obj = FindA("sumanthketharaju", "a")
find_obj.count_char()
