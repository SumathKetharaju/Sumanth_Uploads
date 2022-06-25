"""
write a program to print status of dharshan tickets when the person came to book dharshan tickets,
here dharshan tickets are limted to 50 and after all bookings are completed print dharshan tickets filled
"""

limited_dharshan_tickets = 51
print(limited_dharshan_tickets)
count_of_person = 1

while True:
    print(f"Person {count_of_person} came to book dharshan ticket")
    if count_of_person != limited_dharshan_tickets:
        print(f"Book your ticket here :")
        print(f"person {count_of_person} booked dharshan ticket")
        print()
    else:
        print(f"All dharshan Tickets are filled")
        break
    count_of_person += 1
