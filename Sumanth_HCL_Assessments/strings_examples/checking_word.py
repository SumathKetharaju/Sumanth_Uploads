sample_string = "He is a Business Man america by"

vowels = "aeiou"
words = sample_string.lower().split()

count_of_begin_with_vowel_words = 0
count_of_begin_with_consonant_words = 0

with open("sample.txt", "r") as f:
    data = f.read()
    words_data = data.lower().split()
    for word in words_data:
        if word[0] in vowels:
            print(word)
            count_of_begin_with_vowel_words += 1
        else:
            count_of_begin_with_consonant_words += 1
    print(count_of_begin_with_consonant_words)
    print(count_of_begin_with_vowel_words)


#
# for word in words:
#     if word[0] in vowels:
#         print(word)
#         count_of_begin_with_vowel_words += 1
#     else:
#         count_of_begin_with_consonant_words += 1
# print(count_of_begin_with_consonant_words)
# print(count_of_begin_with_vowel_words)

