from pip._vendor.distlib.compat import raw_input

max=int(raw_input())
i=0
w=0
while (w<max):
    w = w + int(raw_input())
    i+=1

if w > max:
    print (i-1)
else:
    print (i)