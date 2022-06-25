def test_write_ten_lines(test_file):

    print("This test is related to Writing Ten lines")
    num_of_lines_before = sum(1 for line in open(test_file.name))

    for i in range(10):
        test_file.write(f"This is line number {i}")

    test_file.flush()
    num_of_lines_after = sum(1 for line in open(test_file.name))

    assert (num_of_lines_after - num_of_lines_before) == 0
    test_file.close()


def test_field_count(readonly_file):

    print("for read only")
    readonly_file.readline()
    field_count = len(readonly_file.readline().split())
    assert field_count == 4

