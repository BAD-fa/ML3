s = input().split('@')

output = ""

if len(s[0]) > 0 and len(s[-1]) > 0:
    for elm in s[1:-1]:
        if len(elm) < 2:
            print("No Solution")
            break
    else:
        for i in range(len(s) - 1):
            if i:
                output += s[i][:1] + "," + s[i][1:] + "@"
            else:
                output += s[i] + "@"
        output += s[-1]
        print(output)
else:
    print("No Solution")





