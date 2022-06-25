"""
write a  program to show available and not available seats in a cinema hall, here we assume that the cinema hall having
5rows, In each row we have 10 seats the condition one is both row1 and row3 having even number seats are not available to
book our seats & remaining seats are to be available in that rows1,3 respectively and condition two is  remaining 2, 4, 5 rows
having odd number seats are not available to book our seats & remaining seats are to be available in that rows2,4,5respectively
"""
print("This shows available and not available seats in a cinema hall")
row_no = 1
while row_no < 6:
    print(f"------------------------------------- row number : {row_no}  -----------------------------------------")
    seat_no = 1
    while seat_no < 11:
        if row_no == 1 or row_no == 3:
            if seat_no % 2 == 0:
                print(f"seat number {seat_no} is not available but other seats are available")
            else:
                print(f"seat number {seat_no} is available Please Book your seat")
        else:
            if seat_no % 2 != 0:
                print(f"seat number {seat_no} is not available but other seats are available")
            else:
                print(f"seat number {seat_no} is available Please Book your seat")
        seat_no += 1
    row_no += 1
















# list_of_persons = ["Sumanth", "Sasi", "Jafrulla", "Praveen", "Harish"]
# # random.shuffle(list_of_persons)
# print(list_of_persons)
# no_of_seat_rows_in_cinema_hal = 1
# print("Entering into the hall:")
# while no_of_seat_rows_in_cinema_hal < 2:
#     no_of_seats_in_a_row = 1
#     print(f"In row no {no_of_seat_rows_in_cinema_hal}")
#     # random.random(list_of_persons)
#     while no_of_seats_in_a_row <= 5:
#         for person in list_of_persons:
#             # print(f"{no_of_seats_in_a_row} seat is available")
#             print(f"{person} is sitted in seat no {no_of_seats_in_a_row}")
#             no_of_seats_in_a_row += 1
#     no_of_seat_rows_in_cinema_hal += 1





