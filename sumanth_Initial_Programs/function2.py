def greet():
    print("hello")
    print("good morning")

greet()

def add_sub(x, y):
    c = x+y
    d = x-y
    return c, d

result1,result2 = add_sub(12, 13)
print("result1, result2")
