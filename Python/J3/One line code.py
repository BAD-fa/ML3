print(" ".join(sorted([i if ord(i) % 2 else i.upper() for i in input()], reverse=True)))