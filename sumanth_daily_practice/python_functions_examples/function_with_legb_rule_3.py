def house():

    name = "I am Sasi"

    def room():

        name = "I am Sunil"
        print(f"Local: {name}")
    room()
    print(f"Enclosing: {name}")


house()


