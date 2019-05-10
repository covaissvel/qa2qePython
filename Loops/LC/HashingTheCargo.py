string = raw_input()
mylist = string.split(",")
mylist = map(int, mylist)
n = int(raw_input())
hashedlist = []
for i in range(0, len(mylist)):
    if mylist[i] % n == 0:
        hashedlist.append(n)
    else:
        hashedlist.append(mylist[i] % n)

print hashedlist
