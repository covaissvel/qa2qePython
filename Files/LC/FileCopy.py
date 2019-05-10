import os


def filewrite(fileinput, fileoutput):
    with open(fileoutput, 'w') as of:
        with open(fileinput, 'r') as inf:
            of.write(inf.read())


fI = os.path.join('C:/Users/ssubra029c/Documents/CTS/QA2QE/Python/Files', 'file_in.txt')
fO = os.path.join('C:/Users/ssubra029c/Documents/CTS/QA2QE/Python/Files', 'file_out.txt')

filewrite(fI, fO)
