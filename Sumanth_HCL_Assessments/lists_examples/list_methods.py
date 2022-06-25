input_list = [24, 56, 89, 74, 32, 16, "string", 65, 32, 74]

print(f"---------------------------------------Indexing------------------------------------------------------------\n")

print(f"For accessing first element from the list we will use 'input_list[0]' --> {input_list[0]}")
print(f"For accessing seventh element from the list we will use 'input_list[0]' --> {input_list[6]}\n")

print(f"---------------------------------------Nested Indexing-----------------------------------------------------\n")

print(f"For accessing fourth element in the string from the list we will use 'input_list[6][3]' --> {input_list[6][3]}")
print(f"For accessing second element in the string from the list we will use 'input_list[6][3]' --> {input_list[6][1]}\n")

print(f"---------------------------------------Slicing------------------------------------------------------------\n")

print(f"For accessing range of elements from fourth element to seventh element within the list we will use "
      f"'input_list[3:7]' --> {input_list[3:7]}")
print(f"For accessing range of elements from second element to fourth element within the list we will use "
      f"'input_list[1:4]' --> {input_list[1:4]}\n")

print(f"---------------------------------------Negative Indexing---------------------------------------------------\n")

print(f"For accessing last third element from the list we will use 'input_list[-3]' --> {input_list[-3]}")
print(f"For accessing last fifth element from the list we will use 'input_list[-5]' --> {input_list[-5]}\n")

print(f"-------------------------------------Negative Nested Indexing----------------------------------------------\n")

print(f"For accessing range of elements from last fourth element to last second element within the list we will use "
      f"'input_list[-4][-2]' --> {input_list[-4][-2]}\n")
print(f"For accessing range of elements from last fourth element to last first element within the list we will use "
      f"'input_list[-4][-1]' --> {input_list[-4][-1]}\n")

print(f"---------------------------------------Negative Slicing---------------------------------------------------\n")

print(f"For accessing range of elements from last eight element to last third element within the list we will use "
      f"'input_list[-8:-3]' --> {input_list[-8:-3]}\n")

print(f"For accessing range of elements after last fourth element to last element within the list we will use "
      f"'input_list[-4:]' --> {input_list[-4:]}\n")


print(f"************************************** List methods ************************************************\n")

print(f"---------------------------------------append method---------------------------------------------------\n")

print(f"if we want to add an element to the list we will use 'input_list.append(54)' --> \n")
input_list.append(54)
print(f"After adding 54 to given list, then The input list is --> {input_list}\n")

print(f"---------------------------------------extend method---------------------------------------------------\n")

print(f"if we want to add range of elements to the list we will use 'input_list.extend([12, 34, 56, 89])' --> \n")
input_list.extend([12, 34, 56, 89])
print(f"After adding 12, 34, 56, 89 to given list, then The input list is --> {input_list}\n")

print(f"---------------------------------------remove method---------------------------------------------------\n")
print(f"if we want to remove an string from the list we will use 'input_list.remove(\"string\")' --> \n")
input_list.remove("string")
print(f"After removing string from the given list, then The input list is --> {input_list}\n")

print(f"---------------------------------------pop method---------------------------------------------------\n")
print(f"if we want to remove second element from the list we will use 'input_list.pop(1)' --> \n")
input_list.pop(1)
print(f"After removing second element from the given list, then The input list is --> {input_list}\n")
print(input_list.pop(1))
print(f"if we want to print removed second element from the list we will use "
      f"'print(input_list.pop(1))' --> input_list.pop(1)\n")

print(f"---------------------------------------del method---------------------------------------------------\n")
print(f"if we want to delete first element from the list we will use 'del input_list[0]' --> \n")
del input_list[0]
print(f"After removing first element from the given list, then The input list is --> {input_list}\n")

print(f"---------------------------------------sort method---------------------------------------------------\n")
print(f"if we want to sort the elements from the list we will use 'input_list.sort()' --> \n")
input_list.sort()
print(f"After sorting elements from the given list, then The input list is --> {input_list}\n")

print(f"---------------------------------------reverse method---------------------------------------------------\n")
print(f"if we want to reverse the elements from the list we will use 'input_list.reverse()' --> \n")
input_list.reverse()
print(f"After reversing elements from the given list, then The input list is --> {input_list}\n")

print(f"---------------------------------------count method---------------------------------------------------\n")
print(f"if we want to count an element from the list we will use 'print(input_list.count(89))' --> {input_list.count(89)}\n")

print(f"---------------------------------------index method---------------------------------------------------\n")
print(f"if we want to find index of an element from the list we will use 'print(input_list.index(54))' --> {input_list.index(54)}\n")

print(f"---------------------------------------copy method---------------------------------------------------\n")
print(f"if we want to copy all elements from the list we will use 'input_list.copy()' --> {input_list.copy()}\n")


