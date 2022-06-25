#  write a code to print that first unique character and position of that character

input_string = """Python is a powerful general-purpose programming language. It is used in web development, 
data science, creating software prototypes, and so on. Fortunately for beginners, Python has simple easy-to-use syntax. 
This makes Python an excellent language to learn to program for beginners."""

words = input_string.split()

count_of_word = {}

unique_words = []
duplicate_words = []

for word in words:
    if word not in count_of_word:
        count_of_word[word] = 1
    else:
        count_of_word[word] += 1

print(count_of_word)

for word, value in count_of_word.items():
    if value == 1:
        print(word)
        unique_words.append(word)
    else:
        duplicate_words.append(word)

print(unique_words)
print(duplicate_words)
