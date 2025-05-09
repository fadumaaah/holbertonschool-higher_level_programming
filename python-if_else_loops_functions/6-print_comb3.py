#!/usr/bin/python3
for i in range(0, 90):
    if i == 89:
        print(i)
    else:
        firstdigit = i // 10
        lastdigit = i % 10
        if firstdigit != lastdigit:
            if firstdigit < lastdigit:
                print("{:02d} ".format(i), end="")
