import datetime

today_date = datetime.datetime.today()
print(today_date)

date = datetime.date(2021, 7, 29)
print(date)

days_starts_with_0 = datetime.date.weekday(date)
print(days_starts_with_0)

days_starts_with_1 = datetime.date.isoweekday(date)
print(days_starts_with_1)

tdelta = datetime.timedelta(days=7)
print(tdelta)
print(today_date + tdelta)

birthday_date = datetime.date(2021, 6, 11)
print(birthday_date)

# difference = today_date - birthday_date
# print(difference.day)

time = datetime.time(12, 45, 58, 150)
print(time)

date_times = datetime.datetime(2021, 8, 20, 12, 45, 58, 1500)
print(date_times)

date_string = "August 20, 2021"
convert_to_date = datetime.datetime.strptime(date_string, "%B %d, %Y")
print(convert_to_date)
