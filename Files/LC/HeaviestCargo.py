import os
print 'Enter the n value :'
n = int(raw_input())


def readfileAsTuple(file):
    content = []
    with open(file, 'r') as f:
        for i in f.readlines():
            v = i.strip().split("-")
            content.append((v[0].strip(),int(v[1].strip())))
    return content

    #     mylist = [tuple(map(str,i[0]),map(int,i[1])) for i in f]
    # contents = ''
    # if f.mode == 'r':
    #     contents = f.read()
    # return contents
def getKey(item):
    return item[1]


file = os.path.join("C:/Users/ssubra029c/Documents/CTS/QA2QE/readnLines", "readnLines.txt")
contents = readfileAsTuple(file)
print "before :\n", contents
# sorted = sorted(contents, key=getKey)
# # sorted = sorted(contents)
# print "after :\n", sorted

for i in range(len(contents)-n,len(contents),1):
    print contents[i][0],'-',contents[i][1]
# for key in sorted[-n:]:
#     print key, '-', contents[key]

# with open('t3.txt') as f:
#     mylist = [tuple(map(float, i.split(','))) for i in f]

# with open()
