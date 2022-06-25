input_list = [12, 23, 36, 84, 55, 56, 75, 85, 89]


def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]


chunk_size = 2

print(list(split(input_list, chunk_size)))


chunk_size = 2
list_chunked = [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]
print(list_chunked)
