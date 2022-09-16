a, b, c = list(map(int, input().split(' ')))

elv1 = abs(a - 1)
elv2 = abs(b - c) + abs(c - 1)

if elv1 < elv2:
    print(1)
elif elv2 < elv1:
    print(2)
else:
    print(3)

