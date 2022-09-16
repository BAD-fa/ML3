a = [1, 4, 5, 8, 15, 26, 70]

find = 5

for i in a:
    if i == find:
        print(f"find is {i} and index is {a.index(i)}")
        break
