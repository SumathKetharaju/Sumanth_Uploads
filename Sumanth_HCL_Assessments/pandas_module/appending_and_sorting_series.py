import pandas

series_one = pandas.Series([1, 2, 3, 4, 5])
series_two = pandas.Series([1, 3, 5, 7, 9])

print(f"Series one is --> \n{series_one}\n")
print(f"Series two is --> \n{series_two}\n")

# FutureWarning: The series.append method is deprecated and will be removed from pandas in a future version. Use pandas.concat instead.
print(f"""Adding Elements of series_one and series_two using 'series_one.append(series_two)' is --> \n{series_one.append(series_two)}\n""")

# AttributeError: 'Series' object has no attribute 'concat'
# print(f"Adding Elements of series_one and series_two using 'series_one.append(series_two)' is --> \n{series_one.concat(series_two)}\n")

append_series = series_one.append(series_two, ignore_index=True)
print(f"""Adding Elements of series_one and series_two using 
'append_series = series_one.append(series_two, ignore_index=True)' is --> \n{series_one.append(series_two)}\n""")

print(f"To delete an item from the append series using 'append_series.drop(8)' is --> \n{append_series.drop(8)}\n")
print(f"To delete an item from the append series using 'append_series.drop(2)' is --> \n{append_series.drop(2)}\n")

print(f"To delete multiple items from the append series using 'append_series.drop(labels=[5, 7])' is --> \n{append_series.drop(labels=[5, 7])}\n")
print(f"To delete multiple items from the append series using 'append_series.drop(labels=[1, 3, 9])' is --> \n{append_series.drop(labels=[1, 3, 9])}\n")

print(f"To count items from the append series using 'append_series.count()' is --> \n{append_series.count()}\n")

print(f"To Print count of unique items from the append series using 'append_series.nunique()' is --> \n{append_series.nunique()}\n")

print(f"To Print unique items from the append series using 'append_series.unique()' is --> \n{append_series.unique()}\n")

print(f"For sorting the items from the append series using 'append_series.sort_values()' is --> \n{append_series.sort_values()}\n")

append_series.sort_values(inplace=True)

print(f"For sorting the items from the append series using 'append_series.values(inplace=True)' is --> \n{append_series.sort_values(inplace=True)}\n")

print(f"For sorting the items from the append series using 'append_series' is --> \n{append_series}\n")

print(f"For resetting the index from the append series using 'append_series.reset_index()' is --> \n{append_series.reset_index()}\n")

print(f"For resetting the index from the append series using 'append_series.reset_index(drop=True)' is --> \n{append_series.reset_index(drop=True)}\n")
