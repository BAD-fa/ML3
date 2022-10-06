def load_all(address):
    with open(address) as file:
        for line in file:
            yield line


def filter(address, filter_param):
    with open(address) as file:
        for line in file:
            if int(line.split(' ')[3]) % filter_param == 0:
                yield line


my_files = load_all("test.txt")

filtered_file = filter("test.txt", 10)

print(type(my_files))
#
# for i in my_files:
#     print(i)

for j in filtered_file:
    print(j)
