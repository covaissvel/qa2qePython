# from__future__ import print_function

print ("Enter the Numbers in List-1")
string1 = raw_input()
print ("Enter the Numbers in List-2")
string2 = raw_input()

string1 = string1.split()
string2 = string2.split()

list1 = [int(x) for x in string1]
list2 = [int(x) for x in string2]

list3 = []

for i in list1:
    for j in list2:
        if (i * j) % 2 != 0:
            list3.append(i * j)

if len(list3) > 0:
    # print (*list3, sep=' ')
    print ' '.join(map(str, list3))
else:
    print ("No such Elements in the list")