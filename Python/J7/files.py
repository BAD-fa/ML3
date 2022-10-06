import time

my_file = open("test.txt", "w")

for i in range(1000):
    my_file.write(f"this is the {i+20} line\n")
    print(my_file.tell())

my_file.flush()
# my_file.close()
#
#
# my_file.seek(0)
# print(my_file.tell())
#
# for i in range(10):
#     my_file.write(f"this is the {i * 2} line\n")
#     print(my_file.tell())

# print(my_file.read(10))

# print(my_file.readline(12))
# print(my_file.readline(12))

# print(my_file.readlines())

# with open("test.txt") as f:
#     # lines = f.readlines()
#     # for line in lines:
#     #     print(line)
#
#     for line in f:
#         print(line)



'''
mode r: for read only
mode w: for write only
mode a: for write only (append)
mode r+: for read and write
'''
