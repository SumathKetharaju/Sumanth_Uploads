def principal(name, *args):

    print(f"Here principal name is {name} and he is having {args}")
    for arg in args:
        print(arg)
    return f"Here principal name is {name} and he is having following {args}"


principal("Subbarao", "bike", "car", "own house", "apartment")
print(principal("Subbarao", "bike", "car", "own house", "apartment"))
