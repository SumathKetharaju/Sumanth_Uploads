import datetime

date = datetime.date(2021, 7, 29)
print(date)

today = datetime.date.today()
print(today)

day_starts_with_0 = datetime.date.weekday(date)
print(day_starts_with_0)

day_starts_with_1 = datetime.date.isoweekday(date)
print(day_starts_with_1)

tdelta = datetime.timedelta(days=7)
print(tdelta)
print(today + tdelta)

birthday_date = datetime.date(2021, 6, 11)
print(birthday_date)
difference = today - birthday_date
print(difference.total_seconds())

time = datetime.time(9, 45, 55, 1000)
print(time)

date_time = datetime.datetime(2021, 7, 29, 12, 1, 45, 100)
print(date_time)

time_delta = datetime.timedelta(days=7)
print(time_delta)
print(date_time + time_delta)

date_string = "july 29, 2021"
convert_to_date = datetime.datetime.strptime(date_string, "%B %d, %Y")
print(convert_to_date)
