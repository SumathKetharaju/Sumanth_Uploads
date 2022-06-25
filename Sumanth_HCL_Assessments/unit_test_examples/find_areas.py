def triangle(height, base):

    return 0.5 * height * base


def rectangle(length, breadth):

    return length * breadth


def get_perimeter(length, breadth):
    if length == 0 or breadth == 0:
        raise ValueError("Invalid Input!")
    return 2 * (length + breadth)


def square(side):
    return side ** 2
