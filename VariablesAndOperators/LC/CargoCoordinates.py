contLen = int(input())
carLen = int(input())
pos = int(input())

r = int(contLen/carLen)

x = 0

for i in range(r):
    for j in range(r):
        for k in range(r):
            x += 1
            if x == pos:
                print('(',k,',',j,',',i,')')
                continue


