# string = "india is my country and i love my country" find the number of occurance of country by using regex?
import re
input_string = "india is my country and i love my country"
word = "country"
second_word = "india"
capital_word = word.upper()
space = " "


class StringOperations:

    def __init__(self, sample_string, word):
        self.sample_string = sample_string
        self.word = word

    def count_of_word(self):
        # syntax --< re.re.findall(pattern, string)
        word_match = re.findall(self.word, self.sample_string)
        print(f"Syntax of findall method is --> re.findall(pattern, string)")
        print(word_match)
        print(f"The Count of Given Word '{self.word}' from the given String '{self.sample_string}' is --> {(len(word_match))}\n")

    def replace_of_word(self, cap_word):
        # syntax --> re.sub(pattern, replace, string)
        word_replace = re.sub(self.word, cap_word, self.sample_string)
        print(f"Syntax of sub method is --> re.sub(pattern, replace, string)")
        print(f"The String after replacing the word with capitals is --> {word_replace}\n")

    def split_string(self):
        string_split = re.split(space, self.sample_string)
        print(f"Syntax of split method is --> re.split(pattern, string)")
        print(f"The list of words from the given string is --> {string_split}\n")

    def replace_of_word_with_subn(self, word_2, capitalize_word):
        # syntax --> re.subn(pattern, replace, string)
        word_replace_2 = re.subn(word_2, capitalize_word, self.sample_string)
        print(f"Syntax of subn method is --> re.subn(pattern, replace, string)")
        print(f"The String after replacing the word with capitalize method is --> {word_replace_2}\n")


str_oper_obj = StringOperations(input_string, word)
print("------------------------------------- findall method -----------------------------------------------------\n")
str_oper_obj.count_of_word()
print("----------------------------------------- sub method ------------------------------------------------------\n")
str_oper_obj.replace_of_word(capital_word)
print("---------------------------------------------- split method ------------------------------------------------\n")
str_oper_obj.split_string()
print("---------------------------------- subn method -------------------------------------------------------------\n")
str_oper_obj.replace_of_word_with_subn(second_word, second_word.capitalize())


