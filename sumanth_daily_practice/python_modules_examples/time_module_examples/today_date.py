import datetime

today_date = datetime.datetime.today()

print(today_date)

date_string = "27 August, 2021"

convert_to_date = datetime.datetime.strptime(date_string, "%d %B, %Y")

print(convert_to_date)
