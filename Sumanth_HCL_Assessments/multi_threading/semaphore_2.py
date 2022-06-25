import threading
import time

# semaphore = threading.Semaphore(0)
#
# order_num = 0
#
#
# def place_order():
#
#     print(f"Here Order Placed")
#     semaphore.acquire()
#     print(f"The Customer order number is --> {order_num}")
#
#
# def prepare_order():
#
#     global order_num
#     time.sleep(3)
#     order_num += 1
#
#     print(f"Preparing Order number is --> {order_num}")
#     semaphore.release()
#
#
# for i in range(0, 6):
#
#     t1 = threading.Thread(target=place_order)
#     t2 = threading.Thread(target=prepare_order)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
# print(f"Program terminated")

semaphore = threading.Semaphore()
print(semaphore._value)

semaphore.acquire()
print(semaphore._value)


semaphore.release()
print(semaphore._value)

semaphore.release()
print(semaphore._value)

semaphore.release()
semaphore.release()
semaphore.release()
print(semaphore._value)

semaphore = threading.BoundedSemaphore()
print(semaphore._value)

semaphore.acquire()
print(semaphore._value)

semaphore.release()
print(semaphore._value)

# semaphore.release()
# # ValueError: Semaphore released too many times
# print(semaphore._value)
