import re

email = raw_input()
var1 = email.find('@')
username = email[0:var1]
domain = email[var1 + 1:len(email)]
var2 = domain.find('.')
topDomain = domain[var2 + 1:len(domain)]
domain1 = domain[0:var2]
errorList = []

if (topDomain == 'com' or topDomain == 'in' or topDomain == 'edu'):
    status = 'valid'
else:
    status = 'invalid'
    errorList.append('1')

if (len(domain1) > 3):
    status = 'valid'
else:
    status = 'invalid'
    errorList.append('2')

if (re.match("^[a-z0-9_.-]*$", username)):
    if (username.startswith('_') or username.endswith('_') or username.startswith('.') or username.endswith('.') or username.startswith('-') or username.endswith('-')):
        status = 'invalid'
        errorList.append('3')
    else:
        status = 'valid'
else:
    status = 'invalid'
    errorList.append('3')

if (status == 'valid' and len(errorList) <= 0):
    print 'Valid'
else:
    print 'Invalid'
    for x in errorList:
        print x
