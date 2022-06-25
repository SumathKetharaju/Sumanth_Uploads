"""
scenario --> To book a bus ticket
inuput -->
website
bus name
bus number
bus seats
available seats
person booked a seat
available seats
"""
# names = "Sumanth Sasi"
# splitted_names = names.split()

list_of_travels = ["Orange tours and travels"]
booked_seat_numbers = []


def booking(*args):

    if len(args) < 25:

        for name in args:

            chrome = input("please click here to open the chrome: ")
            if chrome == "click":

                website = input("This is the website to book bus tickets, please click here: ")
                if website == "bus ticket booking":

                    print(f"There are many travels are available so you can ping any of those --> {list_of_travels}")
                    selected_travel = input("please select your travel here : ")

                    if selected_travel in list_of_travels:
                        total_seats = 24
                        print(f"Total number of seats --> {total_seats}")
                        print(f"Already booked_seats are --> {booked_seat_numbers}")
                        seat_number = input("Please book your seat here : ")
                        seat_number = int(seat_number)

                        if seat_number in range(1, total_seats+1):
                            if seat_number not in booked_seat_numbers:
                                booked_seat_numbers.append(seat_number)
                                print(f"Seat number {seat_number} is booked for {name}")
                                print(f"Already booked seat numbers are {booked_seat_numbers}")
                            else:
                                print(f"Seat number {seat_number} is already booked, so please select another seat number")
                        else:
                            print("Please enter valid seat numbers between 1 to 24")
                            # seat_number = input("Please book your seat here : ")
                    else:
                        print(f"Please enter available travels like {list_of_travels}")
                else:
                    print("Please enter bus ticket booking only")
            else:
                print("Please enter click only")
    else:
        print("All seats are fulled")


booking("Sumanth", "Sasi")
