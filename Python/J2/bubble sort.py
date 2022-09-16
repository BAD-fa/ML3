a = [20, 3, 12, 2, 40, 1, 32]

for i in range(len(a)):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)