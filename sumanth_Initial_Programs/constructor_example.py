class Computer:

    def __init__(self):
        self.name = "sunil"
        self.age = 21

# by using update method we can update privious age as below
   #def update(self):
    #   self.age = 30


    def compare(self,other):
       if self.age == other.age:
           return True
       else:
           return False


c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")

#c1.name = "sudeer"
#c1.age = 25
#c1.update()

print(c1.name)
print(c2.name)

#print(id(c1))
#print(id(c2))

