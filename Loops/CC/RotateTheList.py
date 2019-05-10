print "Enter the Numbers in List"
string1 = raw_input()
string1 = string1.split()
print "Before Rotating :".strip(" ")
print ' '.join(map(str, string1))
string2 = []
for i in range(1, len(string1)):
    string2.append(string1[i])

string2.append(string1[0])

print "After Rotating :".strip(" ")
print ' '.join(map(str, string2)).strip(" ")