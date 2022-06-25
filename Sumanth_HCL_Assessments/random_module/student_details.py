import random

first_names = ["Mahesh", "Tarak", "Ram", "Arjun", "Sai"]

last_names = ["Babu", "Ramarao", "Charan", "Allu", "Tej"]

street_names = ["Main", "high", "Pearl", "Maple", "Park"]

cities = ["Metropoils", "Eerie", "Kings Landing", "Sunnydale", "Bedrock"]

states = ["AL", "AK", "AZ", "AR", "CA"]

for num in range(10):

    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f"{random.randint(100, 999)}-555-{random.randint(1000, 9999)}"

    street_num = random.randint(100, 999)
    street = random.choice(street_names)
    city = random.choice(cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    address = f"{street_num} {street} St., {city} {state} {zip_code}"
    email = f"{first.lower()}{last.lower()}@gmail.com"
    print(f"{first} {last}\n{phone}\n{address}\n{email}\n")
