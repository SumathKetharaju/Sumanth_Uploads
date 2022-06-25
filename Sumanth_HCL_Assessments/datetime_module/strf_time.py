import datetime
import pytz

date_mountain = datetime.datetime.now(tz=pytz.timezone("US/Mountain"))

print(f"The date in iso format is --> {date_mountain.isoformat()}")

print(f"The date in string format is --> {date_mountain.strftime('%B %d, %Y')}")

date_string = "April 21, 2022"

print(f"The date in datetime format is --> {datetime.datetime.strptime(date_string, '%B %d, %Y')}")
