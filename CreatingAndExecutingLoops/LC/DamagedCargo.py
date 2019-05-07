from pip._vendor.distlib.compat import raw_input

damaged_cargo=[3,4,7,8,11,12,15,16,19,20,23,24,27,28,31,32,35,36,39,40,43,44,47,48,51,52,55,56,59,60]
n=int(raw_input())
if n in damaged_cargo:
    print (damaged_cargo.index(n))
else:
    print ('Safe')