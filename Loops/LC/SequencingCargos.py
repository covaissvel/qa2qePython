data = raw_input()
myList = data.split(",")
myList.sort(reverse=True, key=int)
print myList
count=int(raw_input())
profit=0
for i in range(0,count):
    profit +=int(myList[i])

print profit