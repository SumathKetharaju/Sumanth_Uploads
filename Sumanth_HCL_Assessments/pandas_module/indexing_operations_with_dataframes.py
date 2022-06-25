import pandas

csv_file_path = r"C:\Users\SUMANTH\Desktop\Sumanth_HCL_Assessments\csv_module\countries_dummy_details.csv"

read_csv_data = pandas.read_csv(csv_file_path)

print(f"The CSV file path is --> {csv_file_path}\n")

print(f"The data after reading the csv file using 'read_csv_data = pandas.read_csv(csv_file_path)' is --> \n\n{read_csv_data}\n")

print(f"To print all column Country Names we will use"
      f"'read_csv_data['CountryName']' is --> \n\n{read_csv_data['CountryName']}\n")

print(f"To print only column Population we will use "
      f"'read_csv_data['Population']' is --> \n\n{read_csv_data['Population']}\n")

print(f"To print first five Country Names we will use "
      f"'read_csv_data['Country Name'].head()' is --> \n\n{read_csv_data['CountryName'].head()}\n")

print(f"To print first three BirthRate we will use "
      f"'read_csv_data['BirthRate'].head(3)' is --> \n\n{read_csv_data['BirthRate'].head(3)}\n")

print(f"To print first five DeathRate we will use "
      f"'read_csv_data['DeathRate'].head(5)' is --> \n\n{read_csv_data['DeathRate'].head(5)}\n")

print(f"To print particular column Country Names we will use "
      f"'read_csv_data['Country Name'][10]' is --> \n\n{read_csv_data['CountryName'][10]}\n")

print(f"To print range of column Country Names we will use "
      f"'read_csv_data['Country Name'][3:5]' is --> \n\n{read_csv_data['CountryName'][3:5]}\n")

print(f"To print range of column Country Names with their birthrate we will use "
      f"'read_csv_data['Country Name', 'BirthRate'][1:5]' is --> \n\n{read_csv_data[['CountryName', 'BirthRate']][1:5]}\n")

# TypeError: cannot do slice indexing on RangeIndex with these indexers [CountryName] of type str
# print(f"To print range of column Country Names with their birthrate we dont use
# 'read_csv_data['CountryName' : 'BirthRate'][1:5]' is --> \n\n{read_csv_data['CountryName' : 'BirthRate'][1:5]}\n")

print(f"To print range of column CountryName upto Phones we will use "
      f"'read_csv_data.loc[2:7, 'CountryName' : 'Phones']' is --> \n\n{read_csv_data.loc[2:7, 'CountryName' : 'Phones']}\n")

print(f"To print range of column CountryName upto GDP we will use "
      f"'read_csv_data.loc[2:5, 'CountryName' : 'GDP']' is --> \n\n{read_csv_data.loc[2:5, 'CountryName' : 'GDP']}\n")

print(f"To print range of column CoastlineRatio upto GDP we will use "
      f"'read_csv_data.loc[2:5, 'CoastlineRatio' : 'GDP']' is --> \n\n{read_csv_data.loc[2:5, 'CoastlineRatio' : 'GDP']}\n")

print(f"To print range of column CoastlineRatio upto Area we will use "
      f"'read_csv_data.loc[2:9:2, 'CoastlineRatio' : 'Area']' is --> \n\n{read_csv_data.loc[2:9:2, 'CountryName' : 'Area']}\n")

# TypeError: cannot do slice indexing on Index with these indexers [0] of type int
# print(f"To print range of column CountryNames with their birthrate we will not use
# 'read_csv_data.loc[2:7, 0:4]' is --> \n\n{read_csv_data.loc[2:7, 0:4]}\n")

print(f"To print range of column CountryNames upto  Population Density we will use "
      f"'read_csv_data.loc[2:7, 0:4]' is --> \n\n{read_csv_data.iloc[2:7, 0:4]}\n")


