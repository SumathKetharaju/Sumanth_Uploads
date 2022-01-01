# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string, S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string, S.
#
# For Example:
# String  S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

input_string = input("Enter a string: ")

sunil_score = 0

anil_score = 0

vowel = ["A", "E", "I", "O", "U"]

length_of_string = len(input_string)

for index in range(length_of_string):
    if input_string[index] in vowel:
        sunil_score += length_of_string - index
    else:
        anil_score += length_of_string - index
if sunil_score > anil_score:
    print("sunil", sunil_score)
elif anil_score > sunil_score:
    print("Anil", anil_score)
else:
    print("Draw")

"""that is because, we need the number of words starting with either vowel or consonant.
 So, subtracting the index of the found 'vowel' in this case,
 gives us the number of words starting from that index with a vowel at first. Simple as that."""

