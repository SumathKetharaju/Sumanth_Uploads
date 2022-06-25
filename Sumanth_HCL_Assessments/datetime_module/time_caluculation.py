import datetime

time_now = datetime.time(9, 30, 45, 100000)


print(f"Current mentioned time is --> {time_now}")
print(f"Current mentioned hour is --> {time_now.hour}")
print(f"Current mentioned minute is --> {time_now.minute}")
print(f"Current mentioned seconds is --> {time_now.second}")
print(f"Current mentioned micro seconds is --> {time_now.microsecond}")
