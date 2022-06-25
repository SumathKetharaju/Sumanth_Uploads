import threading


def new_func():

    # to print the total number of thread instances which are currently in active
    print(f"The total number of instances which are currently in active are --> {threading.active_count()}\n")
    # to print the list of the active threads
    print(f"The list of the active threads --> {threading.enumerate()}\n")
    # to print the details of the current threads, it prints current thread object
    print(f"The details of the current thread is --> {threading.current_thread()}")


new_func()
