import xml.etree.ElementTree as ET

import os

xmlFile = os.path.join('C:/Users/ssubra029c/Documents/CTS/QA2QE/Python/Files', 'product.xml')
tree = ET.parse(xmlFile)
root = tree.getroot()

totalCost = 0
for member in root.findall('product'):
    cost = member.find('cost').text
    cost = int(cost)
    totalCost += cost

print 'Total Cost:',totalCost



# tree =ET.parse('product.xml')
# root=tree.getroot()
# print 'id,productName,cost,weight'
# x = 0
#
# for product in root.findall('product'):
#     y = int(product.find('cost').text)
#     x = x + y
# print 'Total Cost:',x
