"""
class --> class is blueprint for the object and by This blueprint we can create multiple numbers of objects.

class definitions begin with a class keyword.

by using class we can construct many instances.

A class creates a new local namespace where all its attributes are defined

The attributes are a characteristic of an object.

An instance is a specific object created from a particular class.
-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------
object --> object is an instantiation of a class(the process of creating the object is called instantiation.)

An object is simply a collection of data (variables) and methods (functions) that act on those data.

This class object allows us to access the different attributes as well as to instantiate new objects of that class.

-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------
Class Variables  -->
Class Variables are the same for all instances of a class.

instance Variables -->
instance Variables are different for every instance of a class.

-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------

self -->
Actually self keyword is used to represent an instance (object) of the given class.

whenever an object calls its method, the object itself is passed as the first argument.

the first argument of the function in class must be the object itself.

If we don't use self argument, we does not  hold the information for multiple objects

-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------

__init__ -->
if you want to initialize instance variables we can use __int__ that is called as constructor
self as first argument
never return anything
whenever an object is created __init__ is called first
"""


class Mobile:

    SHAPE = "Rectangle"

    def __init__(self, name, ram, rom, battery, screensize, camera):
        self.name = name
        self.ram = ram
        self.rom = rom
        self.battery = battery
        self.screensize = screensize
        self.camera = camera

    def battery_usage(self):
        return f"{self.name} mobile gives upto {self.battery} battery usage"

    def ram_usage(self):
        return f"{self.name} mobile gives upto  {self.ram} ram usage"


mobile_1 = Mobile("Vivo", "64GB", "4GB", "3000MAH", "14x12", "20MP")
print(mobile_1)
print(mobile_1.name)
print(mobile_1.battery_usage())

mobile_2 = Mobile("Redmi", "128GB", "8GB", "5000MAH", "16x12", "48MP")
print(mobile_2)
print(mobile_2.name)
print(mobile_2.battery_usage())

