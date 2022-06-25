import datetime

our_date_time = datetime.datetime(2022, 4, 21, 9, 30, 45, 100000)

print(f"Current mentioned datetime is --> {our_date_time}")
print(f"Current mentioned date is --> {our_date_time.date()}")
print(f"Current mentioned time is --> {our_date_time.time()}")

time_delta = datetime.timedelta(days=7)

print(f"date time After 7 days is --> {our_date_time + time_delta}")

time_delta_2 = datetime.timedelta(hours=24)

print(f"date time After 12 hours is --> {our_date_time + time_delta_2}")

today_date_time = datetime.datetime.today()
today_date_time_now = datetime.datetime.now()
today_date_time_utcnow = datetime.datetime.utcnow()

print(f"Today date time is --> {today_date_time}")
print(f"Today date time now is --> {today_date_time_now}")
print(f"Today date time utcnow is --> {today_date_time_utcnow}")
