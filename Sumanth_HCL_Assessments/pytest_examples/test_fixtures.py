import pytest
import os


@pytest.fixture
def test_file():
    print("This Test is related to fixtures")
    f = open("types_of_testing.txt", "a+")
    return f


def test_write_ten_lines(test_file):

    print("This test is related to Writing Ten lines")
    num_of_lines_before = sum(1 for line in open(test_file.name))

    for i in range(10):
        test_file.write(f"This is line number {i}")

    test_file.flush()
    num_of_lines_after = sum(1 for line in open(test_file.name))

    assert (num_of_lines_after - num_of_lines_before) == 0
    test_file.close()


def test_file_size_on_write(test_file):
    print("This test is related to file size")
    size_before = os.stat(test_file.name).st_size
    test_file.write(f"This is Writing One line")

    test_file.flush()
    size_after = os.stat(test_file.name).st_size

    assert (size_after - size_before) > 0
    test_file.close()
