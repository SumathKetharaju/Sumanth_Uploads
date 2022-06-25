import datetime
import pytz

pytz_date_time = datetime.datetime(2022, 4, 22, 9, 30, 45, tzinfo=pytz.UTC)

# print(f"Current pytz date time is --> {pytz_date_time}")

pytz_date_time_now = datetime.datetime.now(tz=pytz.UTC)
print(f"Current pytz date time now is --> {pytz_date_time_now}")

# pytz_date_time_utc_now = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(f"Current pytz UTC date time now is --> {pytz_date_time_now}")

date_mountain = pytz_date_time_now.astimezone(pytz.timezone("US/Mountain"))
# print(f"Current pytz date time now at Mountain is --> {date_mountain}")

# for timezone in pytz.all_timezones:
#     print(f"Time Zone is --> {timezone}")

date_now = datetime.datetime.now()
# print(f"the Current Date Time is --> {date_now}")

date_east = date_now.astimezone(pytz.timezone("US/Eastern"))
print(f"Current pytz date time now at Eastern is --> {date_mountain}")


