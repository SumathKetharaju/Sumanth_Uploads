import threading
import time


class DerivedThread(threading.Thread):

    def run(self):
        time.sleep(2)
        print(f"Hello Small function my name is --> {threading.current_thread().getName()}")


thread_obj = DerivedThread()

thread_obj.start()
thread_obj.join()

print(f"The control returned to --> {threading.current_thread().getName()}")

