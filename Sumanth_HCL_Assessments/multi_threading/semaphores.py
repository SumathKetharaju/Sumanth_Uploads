import threading
import time

# semaphore = threading.Semaphore()


def my_func():

    semaphore.acquire()

    time.sleep(0.1)
    print(f"{threading.currentThread().name} will acquired the semaphore")
    print(f"Semaphore value after {threading.currentThread().name} acquire is --> {semaphore._value}")

    time.sleep(5)
    semaphore.release()
    print(f"Semaphore value after {threading.currentThread().name} release is --> {semaphore._value}")


# t1 = threading.Thread(target=my_func)
# t2 = threading.Thread(target=my_func)

# print(f"Initial semaphore value is --> {semaphore._value}")

# start_time = time.time()
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# end_time = time.time()
#
# print(f"Total Time Between start time and end time is --> {end_time - start_time}")

semaphore = threading.Semaphore(value=3)

t1 = threading.Thread(target=my_func)
t2 = threading.Thread(target=my_func)
t3 = threading.Thread(target=my_func)
t4 = threading.Thread(target=my_func)
t5 = threading.Thread(target=my_func)
t6 = threading.Thread(target=my_func)
t7 = threading.Thread(target=my_func)
t8 = threading.Thread(target=my_func)

start_time = time.time()

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()

end_time = time.time()

print(f"Total Time Between start time and end time is --> {end_time - start_time}")

# semaphore = threading.Semaphore(value=-1)
