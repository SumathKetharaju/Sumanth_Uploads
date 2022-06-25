import threading

amount = 0


def deposit(dep_amount, dep_lock):

    global amount

    for i in range(dep_amount):

        # if we dont use below function it will raise RuntimeError: release unlocked lock
        dep_lock.acquire()

        amount += 1

        dep_lock.release()


def two_deposit_threads(dep_amount):

    lock = threading.Lock()

    t1 = threading.Thread(target=deposit, args=(dep_amount, lock))
    t2 = threading.Thread(target=deposit, args=(dep_amount, lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


# two_deposit_threads(10)
# print(f"The Balance amount is --> {amount}")

# two_deposit_threads(1000)
# print(f"The Balance amount is --> {amount}")

two_deposit_threads(1000000)
print(f"The Balance amount is --> {amount}")
