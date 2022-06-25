import threading
import time


class RegularClass:

    def list_of_items(self):
        mixed_list = [17, 56, "Sumanth", 69, 2.3, True]

        for num in mixed_list:
            print(f"Printing from the Child Thread is --> {num}")
            time.sleep(2)


thread_obj = RegularClass()

thread_obj_call = threading.Thread(target=thread_obj.list_of_items)

thread_obj_call.start()
thread_obj_call.join()

print(f"The control returned to --> {threading.current_thread().getName()}")

