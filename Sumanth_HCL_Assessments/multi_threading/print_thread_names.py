import threading
import time


def small_fun():
    time.sleep(2)
    print(f"Hello Small function my name is --> {threading.current_thread().getName()}")


# thread_1 = threading.Thread(target=small_fun)
# 
# thread_1.start()
# thread_1.join()
#
# print(f"This is Main thread my name is --> {threading.current_thread().getName()}")


thread_2 = threading.Thread(target=small_fun)

print(f"My name is --> {threading.current_thread().getName()}")

thread_2.start()
thread_2.join()

print(f"This is Main thread my name is --> {threading.current_thread().getName()}")
