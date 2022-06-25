import pandas
import pandas as pd

series_of_nums = pd.Series([3, 4, 7, 2, 9])

series_of_letters = pd.Series(["a", "b", "c", "d", "e"])

data_frame_1 = pandas.concat([series_of_nums, series_of_letters], axis=0)
data_frame_2 = pandas.concat([series_of_nums, series_of_letters], axis=1)

print(f"Given Series of numbers when we use 'series_of_nums = pd.Series([3, 4, 7, 2, 9])' are --> \n{series_of_nums}\n")

print(f"Given Series of letters when we use 'series_of_letters = pd.Series(['a, 'b, 'c', 'd , 'e'])' are --> \n{series_of_letters}\n")

print(f"We created dataframe using 'data_frame_1 = pandas.concat([series_of_nums, series_of_letters], axis=0)' is --> \n{data_frame_1}\n")

print(f"We created dataframe using 'data_frame_2 = pandas.concat([series_of_nums, series_of_letters], axis=1)' is --> \n{data_frame_2}\n")

data_frame_3 = pandas.DataFrame({"numbers": series_of_nums, "letter": series_of_letters})

print(f"Newly created dataframe using 'data_frame_3 = pandas.DataFrame('numbers': series_of_nums, 'letters': series_of_letters)' is --> \n{data_frame_3}\n")

csv_file_path = r"C:\Users\SUMANTH\Desktop\Sumanth_HCL_Assessments\csv_module\sample_file.csv"

read_csv_data = pandas.read_csv(csv_file_path)

print(f"The data after reading the csv file using 'read_csv_data = pandas.read_csv(csv_file_path)' is --> \n\n{read_csv_data}\n")

print(f"The data after reading the csv file using 'read_csv_data.head()' is --> \n\n{read_csv_data.head()}\n")

print(f"The data after reading the csv file using 'read_csv_data.head(7)' is --> \n\n{read_csv_data.head(7)}\n")

print(f"The data after reading the csv file using 'read_csv_data.head(3)' is --> \n\n{read_csv_data.head(3)}\n")

print(f"The data after reading the csv file using 'read_csv_data.head(-6)' is --> \n\n{read_csv_data.head(-6)}\n")

print(f"The data after reading the csv file using 'read_csv_data.head(-3)' is --> \n\n{read_csv_data.head(-3)}\n")

print(f"The data after reading the csv file using 'read_csv_data.tail()' is --> \n\n{read_csv_data.tail()}\n")

print(f"The data after reading the csv file using 'read_csv_data.tail(7)' is --> \n\n{read_csv_data.tail(7)}\n")

print(f"The data after reading the csv file using 'read_csv_data.tail(2)' is --> \n\n{read_csv_data.tail(2)}\n")

print(f"The data after reading the csv file using 'read_csv_data.tail(-1)' is --> \n\n{read_csv_data.tail(-1)}\n")

print(f"The data after reading the csv file using 'read_csv_data.tail(-7)' is --> \n\n{read_csv_data.tail(-7)}\n")

requires_columns = ["first_name", "gmail_id"]

read_csv_data_2 = pandas.read_csv(csv_file_path, usecols=requires_columns, decimal=',')

print(f"The data after reading the csv file using 'read_csv_data_2 =pandas.read_csv(csv_file_path), usecols=requires_columns, decimal=','' is --> \n\n{read_csv_data_2}\n")

print(f"The data after reading the csv file using 'read_csv_data_2.head()' is --> \n\n{read_csv_data_2.head()}\n")

print(f"The data after reading the csv file using 'read_csv_data_2.head(1)' is --> \n\n{read_csv_data_2.head(1)}\n")

print(f"The data after reading the csv file using 'read_csv_data_2.head(-2)' is --> \n\n{read_csv_data_2.head(-2)}\n")

print(f"The data after reading the csv file using 'read_csv_data_2.tail()' is --> \n\n{read_csv_data_2.tail()}\n")

print(f"The data after reading the csv file using 'read_csv_data_2.tail(2)' is --> \n\n{read_csv_data_2.tail(2)}\n")

print(f"The data after reading the csv file using 'read_csv_data_2.tail(-3)' is --> \n\n{read_csv_data_2.tail(-3)}\n")


