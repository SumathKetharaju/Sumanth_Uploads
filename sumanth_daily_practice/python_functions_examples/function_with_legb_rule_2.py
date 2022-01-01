# Global variable - It can access from any scope
name = "I am Sumanth"


def house():

    # Local variable - It can access from only local scope
    global name
    name = "I am Sunil"
    print(f"Local: {name}")


house()
print(f"Global: {name}")
