import threading
import time

data_one = 3
data_two = 5


def my_process(lock_one, lock_two):

    global data_one
    global data_two

    lock_one.acquire()
    print(f"Incrementing data one with --> {threading.currentThread().name}")
    data_one += 1
    print(f"After Incrementing data one with --> {threading.currentThread().name} and it will be incremented as --> {data_one}")
    time.sleep(1)

    lock_two.acquire()
    print(f"Incrementing data two with --> {threading.currentThread().name}")
    data_two += 1
    print(f"After Incrementing data one with --> {threading.currentThread().name} and it will be incremented as --> {data_two}")
    time.sleep(1)

    lock_one.release()
    lock_two.release()


lock_one_var = threading.Lock()
lock_two_var = threading.Lock()

t1 = threading.Thread(target=my_process, args=(lock_one_var, lock_two_var))

# Here deadlock will occur because
# t2 = threading.Thread(target=my_process, args=(lock_two_var, lock_one_var))
t2 = threading.Thread(target=my_process, args=(lock_one_var, lock_two_var))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"After incrementing data one with both of the threads is --> {data_one}")
print(f"After incrementing data two with both of the threads is --> {data_two}")
