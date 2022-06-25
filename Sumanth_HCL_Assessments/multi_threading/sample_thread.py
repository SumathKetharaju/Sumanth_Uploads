import threading
import time


# def func():
#
#     print("This is a Sample thread function")

def sleeping_func():

    time.sleep(2)
    print("This is a Sample thread sleeping function")


# thread_1 = threading.Thread()
# thread_1.start()

# thread_1 = threading.Thread(target=func)
# thread_1.start()

# thread_2 = threading.Thread(target=sleeping_func)
# thread_2.start()

# thread_2 = threading.Thread(target=sleeping_func, name="NEW_THREAD")
# thread_2.start()

# to print the total number of instances which are currently in active
print(f"The total number of thread instances which are currently in active are --> {threading.active_count()}")
print()
# to print the list of the active threads
print(f"The list of the active threads --> {threading.enumerate()}")
print()
# to print the details of the current threads, it prints current thread object
print(f"The details of the current thread is --> {threading.current_thread()}")


thread_3 = threading.Thread(target=sleeping_func)
thread_3.start()
thread_3.join()
#
#
print("This is Main Thread")
