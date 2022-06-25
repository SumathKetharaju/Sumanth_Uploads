import threading
import time


def greetings_1():

    for n in range(6):
        print("Hello")
        time.sleep(1)


def greetings_2():

    for n in range(6):
        print("World")
        time.sleep(1)


start_time = time.time()

# greetings_1()
# greetings_2()

thread_1 = threading.Thread(target=greetings_1)
thread_2 = threading.Thread(target=greetings_2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

end_time = time.time()

final_time = end_time - start_time

print(f"Time Taken Between before and after calling two functions is --> {final_time}")
