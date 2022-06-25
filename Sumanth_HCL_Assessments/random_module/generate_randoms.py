import random

value_between_0_and_1 = random.random()
print(f"The Value when we use random method is --> {value_between_0_and_1}\n")

value_between_some_range = random.uniform(1, 10)
print(f"The Value when we use uniform method is --> {value_between_some_range}\n")

int_value_between_some_range = random.randint(1, 6)
print(f"The Integer Value when we use randint method is --> {int_value_between_some_range}\n")

greetings = ["Hello", "Hi", "Hey"]
calling_greetings = random.choice(greetings)
print(f"The item when we use choice method are --> {calling_greetings} Sumanth\n")

colors = ["Red", "Black", "Green"]
number_of_choices = random.choices(colors)
print(f"The items when we use choices method are --> {number_of_choices}\n")

number_of_choices = random.choices(colors, k=10)
print(f"The items when we use choices method with k are --> {number_of_choices}\n")

deck_of_numbers = list(range(1, 15))
print(f"The Given deck of numbers are --> {deck_of_numbers}\n")

random.shuffle(deck_of_numbers)
print(f"The Given deck of numbers after using shuffle are --> {deck_of_numbers}\n")


