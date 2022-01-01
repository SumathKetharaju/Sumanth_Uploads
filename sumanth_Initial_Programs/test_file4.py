"""40.Python program to add two matrices using for loop"""
# x = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# y = [[7, 8, 9],
#      [4, 5, 6],
#      [1, 2, 3]]
#
# result = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]
#
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j] = x[i][j] + y[i][j]
# for r in result:
#     print(r)

"""41.Python program to add two matrices using nested list comprehension"""
# x = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# y = [[7, 8, 9],
#      [4, 5, 6],
#      [1, 2, 3]]
#
# result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
# for r in result:
#     print(r)

"""42.Python program to Transpose a matrix using for loop"""
# x = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# result = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]
#
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[j][i] = x[i][j]
#
# for r in result:
#     print(r)

"""42.Python program to Transpose a matrix using nested list comprehension"""
# x = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# result = [[x[j][i] for j in range(len(x[0]))] for i in range(len(x))]
# for r in result:
#     print(r)

"""43.Python program to multiply two matrices using for loop"""
# x = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# y = [[7, 8],
#      [4, 5],
#      [1, 2]]
#
# result = [[0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0]]
#
# for i in range(len(x)):
#     for j in range(len(y[0])):
#         for k in range(len(y)):
#             result[i][j] += x[i][k] * y[k][j]
# for r in result:
#     print(r)

"""44.Python program to multiply two matrices using list comprehension"""
# x = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# y = [[7, 8],
#      [4, 5],
#      [1, 2]]
#
# result = [[sum(a * b for a, b in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]
# for r in result:
#     print(r)

"""45.Python program to check string is palindrome or not"""
# my_str = "Dad"
# my_str = my_str.casefold()
# rev_str = reversed(my_str)
# if list(my_str) == list(rev_str):
#     print("Given string is a palindrome")
# else:
#     print("Given string is not a palindrome")

"""45.Python program to remove punctuations from a string"""
# punctuations = """!@#$%^&*()/;:'<>?"""
# my_str = "Hello &$This *@! is Sum@anth"
# # my_str = my_str.casefold()
# no_punctuations = ""
# for char in my_str:
#     if char not in punctuations:
#         no_punctuations += char
#
# print(no_punctuations)

"""46.Python program to sort words in Alphabetical order"""
# input_string = "Rohith Sharma was The First Batsman to Hit Double Centuary"
# input_string = input_string.casefold()
# sorted_input_string = sorted(input_string.split())
# print("The sorted words are:")
# for word in sorted_input_string:
#     print(word)

"""47.Python program to illustrate different set operations"""
# E = {1, 2, 3, 5, 6, 5, 98}
# N = {7, 8, 9, 5, 4, 6, 12}
#
# print("The set operations of E and N")
# print("in union are: ", E | N)
# print("in intersection are: ", E & N)
# print("in difference are: ", E - N)
# print("in symmetric difference are: ", E ^ N)

"""48.Python program to count the number of each vowel"""
vowels = "a", "e", "i", "o", "u"
input_str = "Rohith Sharma Was The First Batsman To Hit Two Double Centuaries"
input_str = input_str.casefold()
count = {}.fromkeys(vowels,0)
for char in input_str:
    if char in vowels:
        count[char] += 1
print(count)