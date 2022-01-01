# LEGB rules

# Local, enclosed, global and built_in

# Built-in Scope
from math import pi


pi = 15

def outer():
    pi = 26
    def inner():
        # pi = 7
        nonlocal pi
        pi+=1
        print(pi)

    inner()


outer()

