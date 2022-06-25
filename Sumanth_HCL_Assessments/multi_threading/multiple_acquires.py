import threading

# lock = threading.Lock()


# print(f"first Try ---> {lock.acquire()}")
# print(f"second Try ---> {lock.acquire()}")

# print(f"first Try ---> {lock.acquire()}")
# print(f"second Try ---> {lock.acquire(timeout=3)}")

re_lock = threading.RLock()

print(f"first Try ---> {re_lock.acquire()}")
print(f"second Try ---> {re_lock.acquire()}")
print(f"Third Try ---> {re_lock.acquire()}")
