string1 = raw_input()
string2 = raw_input()

list1 = string1.split(",")
list2 = string2.split(",")

print list1
print list2

list1 = [str(x).lower() for x in list1]
list2 = [str(x).lower() for x in list2]


def findoverlap(list1, list2):
    status = True
    for i in list1:
        if i in list2:
            status = False
    return status


res = findoverlap(list1, list2)
if res:
    print 'Non Overlapping'
else:
    print 'Overlapping'


