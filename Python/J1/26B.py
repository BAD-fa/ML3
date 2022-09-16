# _____________ Answer 1 _______________

# s = input()
#
# counter = 0
#
# for i in range(len(s)):
#     if s[i] == ")":
#         for j in range(i, -1, -1):
#             if s[j] == "(":
#                 counter += 2
#                 s = s[:j] + "0" + s[j+1:i] + "0" + s[i+1:]
#                 break
#
# print(counter)


# _____________ Answer 2 _______________

s = input()

counter = 0
length = 0

for elm in s:
    if elm == "(":
        counter += 1
    elif elm == ")" and counter > 0:
        counter -= 1
        length += 2

print(length)
