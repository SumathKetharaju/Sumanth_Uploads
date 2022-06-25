import pandas as pd

csv_file_path = r"C:\Users\SUMANTH\Desktop\Sumanth_HCL_Assessments\pandas_module\dummy_details.csv"

read_csv_data = pd.read_csv(csv_file_path)

print(f"\nThe CSV file path is --> {csv_file_path}\n")

print(f"The data after reading the csv file using 'read_csv_data = pandas.read_csv(csv_file_path)' is --> \n\n{read_csv_data}\n")

required_columns = ["CountryName", "Population", "Area(sq.ml.)", "GDP", "Literacy", "BirthRate"]

# TypeError: reduction operation 'argmin' not allowed for this dtype when we use idxmin for this below line
# countries = pd.read_csv(csv_file_path, usecols=required_columns, decimal=",")

countries = pd.read_csv(csv_file_path, usecols=required_columns)

print(f"To print first 5 country details we will use 'countries.head()' --> \n\n{countries.head()}\n")

countries.rename(columns={"Area(sq.ml.)": "Area"}, inplace=True)

print(f"To print first 5 country details after changing area column name using "
      f"'countries.rename(columns='Area(sq.ml.)': 'Area', inplace=True)' and 'countries.head()' --> \n\n{countries.head()}\n")

countries.rename(columns={"Literacy": "LiteracyRate", "GDP": "PerCapitaGDP"}, inplace=True)

print(f"To print first 5 country details after changing Literacy column name and GDP column name using "
      f"'countries.rename(columns='Literacy: 'LiteracyRate, 'GDP: 'PerCapitaGDP, inplace=True)' and "
      f"'countries.head()' --> \n\n{countries.head()}\n")

print(f"To Print Missing details in population column we will use "
      f"'countries['Population'].isna().sum()' --> {countries['Population'].isna().sum()}\n")

world_population = countries['Population'].sum()

print(f"To Print World total population we will use 'world_population = countries['Population'].sum()', "
      f"then it gives --> {world_population}\n")

print(f"The number of rows and columns present in our dataframe is --> {countries.shape}\n")

print(f"To Print Missing details in our countries dataframe we will use "
      f"'countries.isna().sum()' --> \n\n{countries.isna().sum()}\n")

countries = countries.dropna()
print(f"To remove Missing details in our countries dataframe we will use 'countries = countries.dropna()'"
      f"and to print remaining we will use 'countries.isna().sum()' --> \n\n{countries.isna().sum()}\n")

print(f"The number of rows and columns present in our dataframe after using dropna is --> {countries.shape}\n")

print(f"The minimum Literacy rate in our countries dataframe using "
      f"'countries.LiteracyRate.min()' is --> {countries.LiteracyRate.min()}\n")

print(f"The minimum BirthRate in our countries dataframe using "
      f"'countries.BirthRate.min()' is --> {countries.BirthRate.min()}\n")

print(f"The maximum Literacy rate in our countries dataframe using "
      f"'countries.LiteracyRate.max()' is --> {countries.LiteracyRate.max()}\n")

print(f"The maximum BirthRate in our countries dataframe using"
      f"countries.BirthRate.max() is --> {countries.BirthRate.max()}\n")

print(f"The row of minimum Literacy rate of country in our countries dataframe is --> {countries.LiteracyRate.idxmin()}")

print(f"The name of minimum Literacy rate of country in our countries dataframe is --> {countries['CountryName'][countries.LiteracyRate.idxmin()]}\n")

print(f"The row of maximum Literacy rate of country in our countries dataframe is --> {countries.LiteracyRate.idxmax()}")

print(f"The name of maximum Literacy rate of country in our countries dataframe is --> {countries['CountryName'][countries.LiteracyRate.idxmax()]}\n")

print(f"{countries['LiteracyRate'] == countries.LiteracyRate.max()}")
