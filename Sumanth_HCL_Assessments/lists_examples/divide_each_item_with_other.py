sample_list = [1, 2, 5, 3, 9, 5, 26, 53, 95]


def list_of_division(input_list):

    if type(input_list) == list:

        print(f"Given Entered List is --> {input_list}\n")

        list_of_division_of_items_with_next_item = []
        last_index = -1

        for index in range(len(input_list)):
            if input_list[index] != input_list[last_index]:
                division_of_item_with_next_item = input_list[index] / input_list[index+1]
                list_of_division_of_items_with_next_item.append(division_of_item_with_next_item)
            else:
                division_of_item_with_that_item = input_list[index] / input_list[index]
                list_of_division_of_items_with_next_item.append(division_of_item_with_that_item)

        print(f"The list of division of items with next item are --> {list_of_division_of_items_with_next_item}\n")
    else:
        print(f'you Entered data is in format of {type(input_list)}, so please enter data in list format only\n')


list_of_division(sample_list)
list_of_division([12, 20, 56, 38, 95, 55, 265, 553, 955])
list_of_division([12, 20, 5.6, 38, 9.5, 55, 265, 55.3, 955])
list_of_division({12, 20, 56, 38, 95, 55, 265, 553, 955})
