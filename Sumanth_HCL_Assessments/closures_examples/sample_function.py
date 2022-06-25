def outer_function():
# def outer_function(msg):

    message = "Hi"
    # message = msg

    def inner_function():

        print(message)

    # return inner_function()
    return inner_function


outer_function()

new_func = outer_function()
print(new_func)
# print(new_func.__name__)
new_func()
# new_func()
# new_func()

# hi_func = outer_function("Hi")
# hello_func = outer_function("Hello")
# print(hi_func)
# print(hi_func.__name__)
# print(hello_func)
# print(hello_func.__name__)
# hi_func()
# hello_func()


