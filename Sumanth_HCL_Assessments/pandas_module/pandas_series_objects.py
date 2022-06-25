import pandas

print(f"Current Version of the Pandas using 'pandas.__version__' is --> {pandas.__version__}\n")

list_of_nums = [3, 4, 7, 2, 9]

print(f"The given list of numbers are --> {list_of_nums}\n")

series_of_nums = pandas.Series(list_of_nums)

print(f"Series of numbers when we use 'pandas.Series(list_of_nums)' are --> \n{series_of_nums}\n")

print(f"To access Second element from pandas series we will use 'series_of_nums[1]' "
      f"then it gives the value as --> {series_of_nums[1]}\n")

print(f"To access third element from pandas series we will use 'series_of_nums[2]' "
      f"then it gives the value as --> {series_of_nums[2]}\n")

index_mask = [0, 3, 4]
index_mask_2 = [1, 2]

print(f"To access multiple elements from pandas series we will use "
      f"'index_mask = [0, 3, 4]' then it gives the values --> \n{series_of_nums[index_mask]}\n")

print(f"To access multiple elements from pandas series we will use "
      f"'index_mask_2 = [1, 2]' then it gives the values --> \n{series_of_nums[index_mask_2]}\n")

boolean_mask = [True, False, False, True, False]
boolean_mask_2 = [True, False, True, False, True]

print(f"To access True elements from pandas series we will use "
      f"'boolean_mask = [True, False, False, True, False]' then it gives the values --> \n{series_of_nums[boolean_mask]}\n")

print(f"To access True elements from pandas series we will use "
      f"'boolean_mask_2 = [True, False, True, False, True]' then it gives the values --> \n{series_of_nums[boolean_mask_2]}\n")

print(f"For printing range of Pandas series we will use 'series_of_nums.index' then it gives --> {series_of_nums.index}\n")

series_of_nums.index = ["a", "b", "c", "d", "e"]

print(f"Series of numbers after changing index values with "
      f"'series_of_nums.index = ['a', 'b', 'c', 'd', 'e']' are --> \n{series_of_nums}\n")

print(f"To access Second element from pandas series we will also use "
      f"'series_of_nums['b']' then it gives the value --> {series_of_nums['b']}\n")

print(f"To access Second element from pandas series we will also use "
      f"'series_of_nums['c']' then it gives the value --> {series_of_nums['c']}\n")

print(f"To access multiple elements from pandas series we will also use "
      f"'series_of_nums[['b', 'c']]' then it gives the values --> \n{series_of_nums[['b', 'c']]}\n")

print(f"To access multiple elements from pandas series we will also use "
      f"'series_of_nums[['a', 'e']]' then it gives the values --> \n{series_of_nums[['a', 'e']]}\n")

dict_of_data = {"a": 3, "b": 4, "c": 7, "d": 2, "e": 9}

print(f"Given Dict of Values are --> {dict_of_data}\n")

series_from_dict = pandas.Series(dict_of_data)

print(f"Series of numbers when we use 'series_from_dict = pandas.Series(dict_of_data)' "
      f"from the given dict are --> \n{series_from_dict}\n")

series_from_dict.name = "Series from Dictionary"

print(f"Series of numbers after changing name of dict with "
      f"'series_from_dict.name = 'Series from Dictionary\''  --> \n{series_from_dict}\n")

series_one = pandas.Series([1, 2, 3, 4, 5])
series_two = pandas.Series([1, 3, 5, 7, 9])

print(f"for checking common Elements in both of them we will use "
      f"'series_one.isin(series_two)' --> \n{series_one.isin(series_two)}\n")

print(f"for printing common Elements in both of them we will use "
      f"'series_one[series_one.isin(series_two)]' --> \n{series_one[series_one.isin(series_two)]}\n")

print(f"for checking different Elements in both of them we will use "
      f"'series_one[~series_one.isin(series_two)]' --> \n{series_one[~series_one.isin(series_two)]}\n")

series_square = series_one.map(lambda x: x * x)

print(f"Square of Series of numbers using 'series_square = series_one.map(lambda x: x * x)' are --> \n{series_square}\n")

print(f"for adding series of elements from both series we will use 'series_one.add(series_two)' --> \n{series_one.add(series_two)}\n")

print(f"Series one is --> \n{series_one}\n")
print(f"Series two is --> \n{series_two}\n")

print(f"After converting Series one items with float is --> \n{series_one.astype('float64')}")
