import pandas as pd

csv_file_path = r"C:\Users\SUMANTH\Desktop\Sumanth_HCL_Assessments\pandas_module\dummy_details.csv"

read_csv_data = pd.read_csv(csv_file_path)

print(f"\nThe CSV file path is --> {csv_file_path}\n")

print(f"The data after reading the csv file using 'read_csv_data = pandas.read_csv(csv_file_path)' is --> \n\n{read_csv_data}\n")

required_columns = ["CountryName", "Population", "Area(sq.ml.)", "GDP", "Literacy", "BirthRate"]
countries = pd.read_csv(csv_file_path, usecols=required_columns)

print(f"To print first 5 country details we will use 'countries.head()' --> \n\n{countries.head()}\n")

print(f"The mean of LiteracyRate in our countries dataframe using"
      f"countries.LiteracyRate.mean() is --> {countries.Literacy.mean()}\n")

print(f"The median of LiteracyRate in our countries dataframe using"
      f"countries.LiteracyRate.median() is --> {countries.Literacy.median()}\n")

print(f"The standard deviation of LiteracyRate in our countries dataframe using"
      f"countries.LiteracyRate.std() is --> {countries.Literacy.std()}\n")

print(f"The quantile of LiteracyRate in our countries dataframe using"
      f"countries.LiteracyRate.quantile() is --> {countries.Literacy.quantile()}\n")

print(f"The 0.5quantile of LiteracyRate in our countries dataframe using"
      f"countries.LiteracyRate.quantile(0.5) is --> {countries.Literacy.quantile(0.5)}\n")

print(f"The 0.25, 0.5, 0.75quantile of LiteracyRate in our countries dataframe using"
      f"countries.LiteracyRate.quantile([0.25, 0.5, 0.75]) is --> \n{countries.Literacy.quantile([0.25, 0.5, 0.75])}\n")

print(f"The mode of LiteracyRate in our countries dataframe using"
      f"countries.LiteracyRate.mode() is --> \n{countries.Literacy.mode()}\n")

print(f"The skew of LiteracyRate in our countries dataframe using"
      f"countries.LiteracyRate.skew() is --> \n{countries.Literacy.skew()}\n")

print(f"The kurtosis of LiteracyRate in our countries dataframe using"
      f"countries.LiteracyRate.kurtosis() is --> \n{countries.Literacy.kurtosis()}\n")

print(f"The correlation between GDP and Literacy is --> \n{countries[['GDP', 'Literacy']].corr()}\n")

print(f"The correlation between GDP and BirthRate is --> \n{countries[['GDP', 'BirthRate']].corr()}\n")

print(f"The correlation between Literacy and BirthRate is --> \n{countries[['Literacy', 'BirthRate']].corr()}\n")

print(f"The correlation of all our countries dataframe is --> \n{countries.corr()}\n")

print(f"The covariance of all our countries dataframe is --> \n{countries.cov()}\n")
