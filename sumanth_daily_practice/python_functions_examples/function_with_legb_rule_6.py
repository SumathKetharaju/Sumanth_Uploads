name = "I am Sumanth"


def house():

    name = "I am Sasi"


    def room():
        
        nonlocal name
        name = "I am Sunil"
        print(f"Local: {name}")
    room()
    print(f"Enclosing: {name}")


house()
print(f"Global: {name}")
