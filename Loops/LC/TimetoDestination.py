# xi = first frieght start time
# li = time of travel between pi-1 and pi ports
# fi = time after a frieght leaves at pi-1 and next frieght starts. duration between two frieghts start time.
noOfPorts = int(raw_input())
values = []
x = []
l = []
f = []
for i in range(0, noOfPorts):
    # values.append(raw_input())
    values = raw_input().split()
    x.append(int(values[0]))
    l.append(int(values[1]))
    f.append(int(values[2]))

time = 0 + l[0]
multiple = 1
for i in range(1, noOfPorts):
    if x[i] > time:
        time = time + abs(x[i] - time)
    else:
        while True:
            temp = x[i] + multiple * f[i]
            multiple += 1
            if temp > time:
                time += temp - time
                break
            else:
                continue
    time += l[i]

print time