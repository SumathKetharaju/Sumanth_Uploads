my_str = "ABCDEF"
test_str = ""
for i in my_str:
    test_str += my_str[0:]
    for j in my_str:
        test_str += my_str[1:] + "A"
        for k in my_str:
            test_str = my_str[2:] + "A" + "B"
            for l in my_str:
                test_str += my_str[3:] + "A" + "B" + "C"
                for m in my_str:
                    test_str += my_str[4:] + "A" + "B" + "C" + "D"




print(test_str)
print(len(test_str))
#print([''.join(str) for str in test_str])

















# import itertools
#
# if __name__ == '__main__':
#     nums = list("ABCDEF")
#     permutations = list(itertools.permutations(nums))
#
#     # Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
#     print([''.join(permutation) for permutation in permutations])