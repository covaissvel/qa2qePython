string = raw_input()


def palindrome(string):
    cleanstring = ''
    revStr = ''
    for i in string:
        if i.isalpha():
            cleanstring = cleanstring + i.lower()
            revStr = i.lower() + revStr

    if cleanstring == revStr:
        print 'Yes'
    else:
        print 'No'


palindrome(string)
