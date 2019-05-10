import os
import xml.etree.ElementTree as ET

fileName = os.path.join('C:/Users/ssubra029c/Documents/CTS/QA2QE/Python/Files', 'candidate.xml')
tree = ET.parse(fileName)
root = tree.getroot()

list= []
for member in root.findall('candidate'):
    name = member.find('candidateName').text
    age = int(member.find('age').text)
    if (age >= 25):
        print name,':', str(age)


# for member in root.findall('candidate'):
#     candidateName = member.find('candidateName').text
#     age = member.find('age').text
#     print 'age =',age
#     print 'candidateName =',candidateName
#     age = int(age)
#     if (age >= 25) :
#         print candidateName , ':',age