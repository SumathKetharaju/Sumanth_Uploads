import datetime

our_mentioned_date = datetime.date(2022, 5, 21)

# raises SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
# our_date = datetime.date(2022, 05, 21)

print(f"Our Mentioned date is --> {our_mentioned_date}")

today_date = datetime.date.today()

print(f"Today date with month and year is --> {today_date}")
print(f"Today date is --> {today_date.day}")
print(f"This month is --> {today_date.month}")
print(f"This year is --> {today_date.year}")

today_weekday = datetime.date.today()

print(f"Weekday of today is --> {today_weekday.weekday()}")
print(f"IsoWeekday of today is --> {today_weekday.isoweekday()}")

time_delta = datetime.timedelta(days=7)

print(f"date After 7 days is --> {today_date + time_delta}")
print(f"date before 7 days is --> {today_date - time_delta}")

independence_day_date = datetime.date(2022, 8, 15)
days_from_today_to_till_independence_day = independence_day_date - today_date

print(f"The days from today to my birthday is --> {days_from_today_to_till_independence_day}")
print(f"The number of days from today to my birthday is --> {days_from_today_to_till_independence_day.days}")
print(f"The number of seconds from today to my birthday is --> {days_from_today_to_till_independence_day.total_seconds()}")

birthday_date = datetime.date(2022, 6, 11)
days_from_today_to_till_birthday = birthday_date - today_date

print(f"The days from today to my birthday is --> {days_from_today_to_till_birthday}")
print(f"The number of days from today to my birthday is --> {days_from_today_to_till_birthday.days}")
print(f"The number of seconds from today to my birthday is --> {days_from_today_to_till_birthday.total_seconds()}")
