def sqrt(x):

    guess = x
    i= 0
    while guess * guess != x and i < 20:
        guess = (guess + x/guess)/2.0
        i += 1
    return guess

def main():
    #print(sqrt(9))
    #print(sqrt(5))
    #print(sqrt(-1))
    try:
        print(sqrt(9))
        print(sqrt(5))
        print(sqrt(-1))
        print("this is never print")
    except ZeroDivisionError:
        print("cannot compute a sqare root of a negative number")
        print("program execution normally execute here")
if __name__ == "__main__":
    main()