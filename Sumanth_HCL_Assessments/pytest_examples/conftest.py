import pytest
import os


@pytest.fixture
def write_file():
    print("This Test is related to conftext fixtures")
    f = open("types_of_testing.txt", "w+")

    for i in range(10):
        f.write(f"This is in line number {i}")

    f.flush()

    yield f

    print("Closing File")
    f.close()


@pytest.fixture
def readonly_file():
    print("This is read only file")
    f = open("types_of_testing.txt", "w+")
    for i in range(10):
        f.write(f"This is line {i}")
    f.close()
    f = open("types_of_testing.txt.txt", "r")
    yield f
    print("Closing file")
    f.close()

