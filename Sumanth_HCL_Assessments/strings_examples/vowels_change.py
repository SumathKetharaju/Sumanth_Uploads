# sample_string = "He is a Business Mmn"
sample_string = "my name is AL SWEIGART and i am 4,000 year old bbc"

expected_string = ""
zero_index = 0
first_index = 1
vowels = "aeiouAEIOU"
words = sample_string.split()
add_to_vowel_word = "yay"
add_to_consonants_word = "ay"

for word in words:
    if word.isalpha():
        if word.isupper():
            if word[zero_index] in vowels:
                # print(word)
                word += add_to_vowel_word.upper()
                expected_string += word + " "
            elif word[zero_index] not in vowels and word[first_index] not in vowels:
                # print(word[:zero_index+2])
                word += word[zero_index] + word[first_index] + add_to_consonants_word.upper()
                word = word[first_index+1:]
                # print(word)
                expected_string += word + " "
            elif word[zero_index] not in vowels:
                # print(word)
                word += word[zero_index] + add_to_consonants_word.upper()
                word = word[zero_index+1:]
                # print(word)
                expected_string += word + " "
        else:
            if word[zero_index] in vowels:
                # print(word)
                word += add_to_vowel_word
                expected_string += word + " "
            elif word[zero_index] not in vowels and word[first_index] not in vowels:
                # print(word[:zero_index+2])
                word += word[zero_index] + word[first_index] + add_to_consonants_word
                word = word[first_index+1:]
                # print(word)
                expected_string += word + " "
            elif word[zero_index] not in vowels:
                # print(word)
                word += word[zero_index] + add_to_consonants_word
                word = word[zero_index+1:]
                # print(word)
                expected_string += word + " "
    else:
        expected_string += word + " "


print(expected_string)
