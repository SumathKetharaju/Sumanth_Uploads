input_single_matrix = [12, 54, 63]
input_single_matrix_2 = [1, 2, 3]

addition_of_two_lists = []
subtraction_of_two_lists = []
multiplication_of_two_lists = []
division_of_two_lists = []

for index in range(len(input_single_matrix)):
    addition_of_items = input_single_matrix[index] + input_single_matrix_2[index]
    subtraction_of_items = input_single_matrix[index] - input_single_matrix_2[index]
    multiplication_of_items = input_single_matrix[index] * input_single_matrix_2[index]
    division_of_items = input_single_matrix[index] // input_single_matrix_2[index]
    addition_of_two_lists.append(addition_of_items)
    subtraction_of_two_lists.append(subtraction_of_items)
    multiplication_of_two_lists.append(multiplication_of_items)
    division_of_two_lists.append(division_of_items)

print(f"The Addition of Two lists {input_single_matrix} and {input_single_matrix_2} is --> {addition_of_two_lists}")
print(f"The Subtraction of Two lists {input_single_matrix} and {input_single_matrix_2} is --> {subtraction_of_two_lists}")
print(f"The Multiplication of Two lists {input_single_matrix} and {input_single_matrix_2} is --> {multiplication_of_two_lists}")
print(f"The Division of Two lists {input_single_matrix} and {input_single_matrix_2} is --> {division_of_two_lists}")

