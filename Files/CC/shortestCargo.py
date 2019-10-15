import os

filename = os.path.join('C:/Users/ssubra029c/Documents/CTS/QA2QE/Python/Files', 'text.txt')
f = open(filename, 'r')
cc = f.readlines()
myList = []
for line in cc:
    tmp = line.strip()
    tmp1 = str(len(tmp)) + ' ' + tmp
    myList.append(tmp1)
f.close()

myList.sort()
shortCargo = int(myList[0][0])

for items in myList:
    str1 = items.split(' ')
    if (int(str1[0]) <= shortCargo):
        print (str1[1])

