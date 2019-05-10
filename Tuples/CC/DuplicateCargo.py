string = raw_input()
list1 = string.split(",")
list1 = [int(x) for x in list1]
cleanlist = []
for i in list1:
    if i not in cleanlist:
        cleanlist.append(i)

tuple = tuple(cleanlist)
print tuple