import time


def sample(func):

    print(f"This is starting time {time.time()}")
    print("This function can be decorated")
    return func

@sample
def sample_2():
    print(f"This first line")
    print(f"This is second line")
    print(f"This is final time {time.time()}")


sample_2()
