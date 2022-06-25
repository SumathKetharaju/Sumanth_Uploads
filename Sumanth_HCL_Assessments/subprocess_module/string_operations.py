"""
string --> why we use strings
difference between single cotes and double cotes
when we use index with example
when we use slicing with example
why we dont use 0 in negative index
how to print string in reverse order
get method in string is valid or not --> homework
count
difference between find and index
strip
lstrip
rstrip
split
join
how to generate random password
string module
random module
"""

input_string = "This is Pycharm IDE"
print("------------------------------------------Indexing-------------------------------------------------------------")
print(f"Given string is --> {input_string}")
print(f"length of given string is --> {len(input_string)}")
print(f"we can access character using positive index like input_string[0] --> {input_string[0]}")
print(f"we can access character using positive index like input_string[9] --> {input_string[9]}")
print(f"we can access character using positive index like input_string[18] --> {input_string[18]}")
print(f"we can access character using negative index like input_string[-1] --> {input_string[-1]}")
print(f"we can access character using negative index like input_string[-19] --> {input_string[-19]}")
print("-------------------------------------------Slicing-------------------------------------------------------------")
print(f"Given string is --> {input_string}")
print(f"length of given string is --> {len(input_string)}")
print(f"we can access range of characters using positive slicing like input_string[0:4] --> {input_string[0:4]}")
print(f"we can access range of characters using positive slicing like input_string[5:7] --> {input_string[5:7]}")
print(f"we can access range of characters using positive slicing like input_string[8:15] --> {input_string[8:15]}")
print(f"we can access range of characters using positive slicing like input_string[16:19] --> {input_string[16:19]}")
print(f"we can access range of characters using positive slicing like input_string[0::1] --> {input_string[0::1]}")
print(f"we can access range of characters using positive slicing like input_string[0::2] --> {input_string[0::2]}")
print(f"we can access range of characters using positive slicing like input_string[0::3] --> {input_string[0::3]}")
print(f"we can access range of characters using positive slicing like input_string[0:4:1] --> {input_string[0:4:1]}")
print(f"we can access range of characters using positive slicing like input_string[0:4:2] --> {input_string[0:4:2]}")
print(f"we can access range of characters using positive slicing like input_string[0:4:3] --> {input_string[0:4:3]}")
print(f"we can access range of characters using positive slicing like input_string[8:15:1] --> {input_string[8:15:1]}")
print(f"we can access range of characters using positive slicing like input_string[8:15:1] --> {input_string[8:15:1]}")
print(f"we can access range of characters using positive slicing like input_string[8:15:2] --> {input_string[8:15:2]}")
print(f"we can access range of characters using positive slicing like input_string[8:15:3] --> {input_string[8:15:3]}")
print(f"we can access range of characters using positive slicing like input_string[9:15] --> {input_string[9:15]}")
print(f"we can access range of characters using positive slicing like input_string[9:15:5] --> {input_string[9:15:5]}")
print(f"we can access range of characters using positive slicing like input_string[:] --> {input_string[:]}")
print(f"we can access range of characters using positive slicing like input_string[0:] --> {input_string[0:]}")
print(f"we can access range of characters using positive slicing like input_string[:19] --> {input_string[:19]}")
print(f"we can access range of characters using positive slicing like input_string[::] --> {input_string[::]}")
print(f"we can access range of characters using positive slicing like input_string[:5] --> {input_string[:5]}")
print(f"we can access range of characters using positive slicing like input_string[5:] --> {input_string[5:]}")
print(f"we can access range of characters using negative slicing like input_string[:-1] --> {input_string[:-1]}")
print(f"we can access range of characters using negative slicing like input_string[:-4] --> {input_string[:-4]}")
print(f"we can access range of characters using negative slicing like input_string[-11:-4] --> {input_string[-11:-4]}")
print(f"we can access range of characters using negative slicing like input_string[-3:] --> {input_string[-3:]}")
print(f"we can access range of characters using negative slicing like input_string[-14:-12] --> {input_string[-14:-12]}")
print(f"we can access range of characters using negative slicing like input_string[-19:-15] --> {input_string[-19:-15]}")
print("-----------------------------------------String in reverse order----------------------------------------------")
print(f"Given string is --> {input_string}")
print(f"length of given string is --> {len(input_string)}")
print(f"Given string in reverse order is input_string[::-1] --> {input_string[::-1]}")
print(f"Given string in reverse order is input_string[::-2] --> {input_string[::-2]}")
print(f"Given string in reverse order is input_string[::-3] --> {input_string[::-3]}")
print("---------------------------------------count of char-----------------------------------------------------------")
print(f"Given string is --> {input_string}")
print(f"length of given string is --> {len(input_string)}")
print(f"Count of particular character in the given string is input_string.count('i') --> {input_string.count('i')}")
print(f"Count of particular character in the given string is input_string.count('s') --> {input_string.count('s')}")
print(f"Count of particular character in the given string is input_string.count('P') --> {input_string.count('P')}")
print("----------------------------------------index of char---------------------------------------------------------")
print(f"Given string is --> {input_string}")
print(f"length of given string is --> {len(input_string)}")
print(f"index of particular character in the given string is input_string.index('P') --> {input_string.index('P')}")
print(f"index of particular character in the given string is input_string.index('i') --> {input_string.index('i')}")
print(f"index of particular character in the given string is input_string.index('D') --> {input_string.index('D')}")
print(f"index of particular character in the given string is input_string.find('D') --> {input_string.find('D')}")
print(f"index of particular character in the given string is input_string.find('h') --> {input_string.find('h')}")
print(f"index of particular character in the given string is input_string.find('m') --> {input_string.find('m')}")
print("-------------------------------------strip of char------------------------------------------------------------")
sample_string = " & This is Pycharm IDE & I am Pra@cticing Strings &"
print(f"Given string is --> {sample_string}")
print(f"length of given string is --> {len(sample_string)}")
print(f"strip of character at the start, end of given string is input_string.strip(' &') --> {sample_string.strip(' &')}")
print(f"strip of character at the start of the given string is input_string.rstrip(' &') --> {sample_string.rstrip(' &')}")
print(f"strip of character at the end of the given string is input_string.lstrip(' &') --> {sample_string.lstrip(' &')}")
print("------------------------------------split---------------------------------------------------------------------")
sample_string = " & This is Pycharm IDE & I am Pra@cticing Strings &"
print(f"Given string is --> {sample_string}")
print(f"length of given string is --> {len(sample_string)}")
print(f"split of given string is input_string.split() --> {sample_string.split()}")
# print(f"split of given string is input_string.split('') --> {input_string.split('')}")   # ValueError: empty separator
print(f"split of given string is input_string.split('&') --> {sample_string.split('&')}")
print(f"split of given string is input_string.split('is') --> {sample_string.split('is')}")
print("----------------------------------------join------------------------------------------------------------------")
# sample_string = " & This is Pycharm IDE & I am Pra@cticing Strings &"
print(f"Given string is --> {sample_string}")
print(f"length of given string is --> {len(sample_string)}")
print(f"split of given string is input_string.split() --> {sample_string.split()}")
print(f"split of given string is ''.join(sample_string) --> {''.join(sample_string)}")
print(f"split of given string is ' '.join(sample_string) --> {' '.join(sample_string)}")
print(f"split of given string is '*'.join(sample_string) --> {'*'.join(sample_string)}")
print("---------------------------------------------------------------------------------------------------------------")


