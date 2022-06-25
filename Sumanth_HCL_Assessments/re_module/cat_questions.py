# 1 --> it should not start with digits
# 2 --> it should not have any symbols before @gmail
"""
@examplegmail.com not valid
example123@gmail.com valid
1example23@gmail.com not
@example.example@gmail.com not
example.example@gmail.com not
example23@gail.com not valid"""

# import re
# input_gmail = input("Enter a valid gmail")
#
# gmail_pattern = re.compile(r"^[A-Za-z][\w]+@gmail\.com$")
# gmail_match = gmail_pattern.search(input_gmail)
#
# if gmail_match:
#     print(f"It is valid gmail --> {gmail_match.group()}")
# else:
#     print(f"It is not valid gmail")

# isec --> send
# 2sec --> anither

import threading
import time


def first_operation():
    time.sleep(1)
    print(f"This is First one")


def second_operation():
    time.sleep(2)
    print(f"This is Second one")


thread_1 = threading.Thread(first_operation())
thread_2 = threading.Thread(second_operation())

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

