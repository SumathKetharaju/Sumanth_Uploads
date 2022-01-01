path = r"C:\Users\SUMANTH\Desktop\sumanth_daily_practice\python_modules_examples\os_module_example\sample.txt"

with open(path, "w") as f:
    data = """Object Oriented Programming
            Python is a multi-paradigm programming language. It supports different programming approaches.
            One of the popular approaches to solve a programming problem is by creating objects.
            This is known as Object-Oriented Programming (OOP).
            """
    f.write(data)
