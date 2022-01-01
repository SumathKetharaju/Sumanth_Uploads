def principal(name, **kwargs):

    print(f"Here principal name is {name} and he is having {kwargs}")
    for kwarg in kwargs:
        print(kwarg)
    return "Here principal name is {name} and he is having following {kwargs}"


principal("Subbarao", bike="Honda bike", car="Rollsroyals", own_house="Duplex", apartment="Thriple bed room flat")
