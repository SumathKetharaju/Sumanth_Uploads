
def sample_function(a, b, c, d, e):
    sum_result=a+b+c+d+e
    print(sum_result)

input_string  =  input("Enter two values to be added?")
#
input_values=input_string.split(" ")
print(input_values)

input_list = []

for i in range(len(input_values)):
    input_list.append(int(input_values[i]))

print(input_list)
sample_function(input_list[0],input_list[1],input_list[2],input_list[3],input_list[4])

# to- do get use of *args for mulitple numbers


