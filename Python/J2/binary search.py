a = [1, 4, 5, 8, 15, 26, 70]
temp = a.copy()

find = 2

while True:
    mid = len(temp) // 2
    if len(temp) > 1:
        if temp[mid] == find:
            print(f"find is {temp[mid]} and index is {a.index(temp[mid])}")
            break
        elif temp[mid] < find:
            temp = temp[mid:]
        elif temp[mid] > find:
            temp = temp[:mid]
    else:
        print("not Found")
        break
