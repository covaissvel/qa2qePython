	#List of Tuples
import datetime
numOfRecords = int(raw_input())
name = []
dateList = []
for i in range (0,numOfRecords) :
    var1 = raw_input()
    temp = var1.split(',')
    name.append(temp[0])
    dateList.append(temp[1])
    i += 1

dateInput = raw_input()
dateInput = datetime.datetime.strptime(dateInput,'%d-%m-%Y')

myTuple = zip(name,dateList)
print myTuple

for list in range (0, len(myTuple)) :
    recordDate = datetime.datetime.strptime(myTuple[list][1],'%d-%m-%Y')
    if (recordDate > dateInput) :
        print myTuple[list][0]
