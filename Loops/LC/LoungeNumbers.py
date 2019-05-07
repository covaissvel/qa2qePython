mystring = raw_input()
mylist = mystring.split(",")
find = raw_input()


for i, elem in enumerate(mylist,1):
        if elem == find:
            print i

if not find in mylist:
        print 0