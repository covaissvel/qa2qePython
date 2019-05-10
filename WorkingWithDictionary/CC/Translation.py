string1 = raw_input()
words = string1.split(",")

thisDict = {}
for i in range(0, len(words)):
    key = words[i].split()[0]
    value = words[i].split()[1]
    thisDict[key] = value

string2 = raw_input()
words = string2.split()
conv = ''
status = True
for j in range(0, len(words)):
    if words[j] not in thisDict:
        status = False
    else:
        conv += ' '+ thisDict[words[j]]

if status:
    print conv.lstrip()
else:
    print 'The sentence cannot be translated'

