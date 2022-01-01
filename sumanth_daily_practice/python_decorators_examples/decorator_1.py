def person_details(func):

    print("My name is sumanth")
    func()
    print("My father name is Srinivasulu")
    print("My father name is Sujatha")



@person_details
def private_details():

    print("My qualification is Btech")
    print("My adhar_number is xxxxxxxxxxxxx")
    print("My adhar_number is xxxxxxxxxxxx")


person_details(func=private_details)
