import pandas

csv_file_path = r"C:\Users\SUMANTH\Desktop\Sumanth_HCL_Assessments\csv_module\countries_dummy_details.csv"

countries_data = pandas.read_csv(csv_file_path)

print(f"The CSV file path is --> {csv_file_path}\n")

print(f"The Countries details from the csv file using 'countries_data = pandas.read_csv(csv_file_path)' are --> \n\n{countries_data}\n")

countries_data["New_Area"] = countries_data["Area(sq.ml.)"] * 1.609 * 1.609


print(f"The Countries details after creating New area using "
      f"'countries_data['New_Area'] = countries_data['Area(sq.ml.)'] * 1.609 * 1.609' are --> \n\n{countries_data}\n")

print(f"The First Five Countries details after creating New area using "
      f"'countries_data.head()' are --> \n\n{countries_data.head()}\n")

print(f"The Last Five Countries details after creating New area using "
      f"'countries_data.tail()' are --> \n\n{countries_data.tail()}\n")

print(f"The Countries details after dropping Area(sq.ml.) using "
      f"'countries_data.drop(labels=['Area(sq.ml.)'], axis=1)' are --> \n\n{countries_data.drop(labels=['Area(sq.ml.)'], axis=1)}\n")

print(f"The First Five Countries details after dropping Area(sq.ml.) using "
      f"'countries_data.head()' are --> \n\n{countries_data.head()}\n")

print(f"The Last Five Countries details after creating New area using "
      f"'countries_data.tail()' are --> \n\n{countries_data.tail()}\n")

print(f"shape of Countries(Number of Row and columns) details using 'countries_data.shape' is --> {countries_data.shape}\n")

print(f"print Missing Countries details using 'countries_data.isna()' are --> \n\n{countries_data.isna()}\n")

print(f"To Print number of Missing Countries details using 'countries_data.isna().sum()' are --> \n\n{countries_data.isna().sum()}\n")

countries_data = countries_data.dropna()

print(f"To Print countries details after dropping Missing Countries details using "
      f"'countries_data = countries_data.dropna()' are --> \n\n{countries_data}\n")

print(f"To Print number of Missing Countries details after dropping Missing Countries details using"
      f"'countries_data.isna().sum()' are --> \n\n{countries_data.isna().sum()}\n")

print(f"shape of Countries(Number of Row and columns) details after dropping Missing Countries details using "
      f"'countries_data.shape' is --> {countries_data.shape}\n")

print(f"To Print First five area details we will use 'countries_data['New_Area'].head()' --> \n\n{countries_data['New_Area'].head()}\n")

print(f"To Print last three area details we will use 'countries_data['New_Area'].tail(3)' --> \n\n{countries_data['New_Area'].tail(3)}\n")

print(f"To Print First five area details we will also use 'countries_data.New_Area.head()' --> \n\n{countries_data.New_Area.head()}\n")

countries_data.New_Area = countries_data.New_Area.apply(lambda x: '%.4f' % x)

print(f"To Print First five area details after changing using "
      f"'countries_data.New_Area = countries_data.New_Area.apply(lambda x: '%.4f' % x)' --> \n\n{countries_data.New_Area.head()}\n")

print(f"To Print last five area details after changing using "
      f"'countries_data.New_Area = countries_data.New_Area.apply(lambda x: '%.4f' % x)' --> \n\n{countries_data.New_Area.tail()}\n")
