class Iterable:

    def __init__(self, input_num):
        self.input_num = input_num


    def count_of_a_num(self, input_num):
        sample_string = "uyfuytyt"
        count = 0
        example = Iterable
        for num in example:
            if num == input_num:
                count += 1
        print(f"count of given character {input_num} is --> {count}")


# sample = Iterable()
# example.count_of_a_num("u")


sample_sting = "SumanthSumanth"
print(sample_sting.count("S"))
