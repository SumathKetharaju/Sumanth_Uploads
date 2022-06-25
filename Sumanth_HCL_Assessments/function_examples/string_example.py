def length_of_string(string):
    if type(string) == str:
        count_of_string = 0
        for char in string:
            count_of_string += 1
        # print(f"The length of the given String {string} is --> {count_of_string}")
        return f"The length of the given String {string} is --> {count_of_string}"
    else:
        # print(f"your entered wrong data that is in {type(string)} format, So Please enter Valid string")
        return f"your entered wrong data that is in {type(string)} format, So Please enter Valid string"


# length_of_string("sumanth")
print(length_of_string("Sumanth"))
print(length_of_string("Hari Krishna"))
print(length_of_string([1, 2, 3]))


def len_of_string_without_space(string):
    if type(string) == str:
        count_of_string = 0
        special_characters = " !@#$%^&*:<>?+-.,;"
        for char in string:
            if char not in special_characters:
                count_of_string += 1
        # print(f"The length of the given String {string} without considering space is --> {count_of_string}")
        return f"The length of the given String {string} without considering space is --> {count_of_string}"
    else:
        # print(f"your entered wrong data that is in {type(string)} format, So Please enter Valid string")
        return f"your entered wrong data that is in {type(string)} format, So Please enter Valid string"


# len_of_string_without_space("Sumanth")
print(len_of_string_without_space("Sumanth"))
print(len_of_string_without_space("Hari Krishna"))
print(len_of_string_without_space([1, 2, 3]))


# def repeated_char(string):
#     if type(string) == str:
#         count_of_string = 0
#         special_characters = " !@#$%^&*:<>?+-.,;"
#         for char in string:
#             if char not in special_characters:
#                 count_of_string += 1
#         # print(f"The length of the given String {string} without considering space is --> {count_of_string}")
#         return f"The length of the given String {string} without considering space is --> {count_of_string}"
#     else:
#         # print(f"your entered wrong data that is in {type(string)} format, So Please enter Valid string")
#         return f"your entered wrong data that is in {type(string)} format, So Please enter Valid string"
#
#
# # len_of_string_without_space("Sumanth")
# print(len_of_string_without_space("Sumanth"))
# print(len_of_string_without_space("Hari Krishna"))
# print(len_of_string_without_space([1, 2, 3]))
