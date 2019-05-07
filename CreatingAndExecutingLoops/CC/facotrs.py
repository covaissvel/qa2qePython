from pip._vendor.distlib.compat import raw_input

n = int(raw_input())

list = []

for i in range(1, n + 1):
    if n % i == 0:
        list.append(i)

#print("The factors of ", n, " are ", *list, sep=",")

