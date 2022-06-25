# sample_string = "He is a Business Mmn"
sample_string = "my name is AL SWEIGART and i am 4,000 year old"

expected_string = ""
zero_index = 0
first_index = 1
vowels = "aeiouAEIOU"
words = sample_string.split()
add_to_vowel_word = "vowel"
add_to_consonants_word = "consonant"
add_to_consonants_cluster_word = "consonant_cluster"

for word in words:
    if word.isalpha():
        # print(word.isalpha(), word)
        if word.isupper():
            # print(word.isupper(), word)
            if word[zero_index] in vowels:
                # print(word)
                word += add_to_vowel_word.upper()
                expected_string += word + " "
            elif word[zero_index] not in vowels and word[first_index] not in vowels:
                # print(word[:zero_index+2])
                word += word[zero_index] + word[first_index] + add_to_consonants_cluster_word.upper()
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
            # print(word.islower(), word)
            if word[zero_index] in vowels:
                # print(word)
                word += add_to_vowel_word
                expected_string += word + " "
            elif word[zero_index] not in vowels and word[first_index] not in vowels:
                # print(word[:zero_index+2])
                word += word[zero_index] + word[first_index] + add_to_consonants_cluster_word
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
