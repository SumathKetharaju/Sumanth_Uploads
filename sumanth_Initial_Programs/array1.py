from array import *
arr = array('i',[])
n = int(input("enter length of array "))
for i in range(n):
    x = int(input("enter the next value "))
    arr.append(x)
print(arr)


vals = int(input("enter the value u want to search "))
k = 0
for e in arr:
    if e == vals:
        print(k)
        break
    k += 1
print(arr.index(vals))
