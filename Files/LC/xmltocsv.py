import os
import xml.etree.ElementTree as ET
import csv

filename = os.path.join('C:/Users/ssubra029c/Documents/CTS/QA2QE/Python/Files', "product.xml")
tree = ET.parse(filename)
root = tree.getroot()

# open a file for writing
ofile = os.path.join('C:/Users/ssubra029c/Documents/CTS/QA2QE/Python/Files', "product.csv")
product_data = open(ofile, 'w')

# create the csv writer object

csvwriter = csv.writer(product_data)
product_head = []

count = 0
for member in root.findall('product'):
    product = []
    if count == 0:
        id = member.find('id').tag
        product_head.append(id)
        name = member.find('productName').tag
        product_head.append(name)
        cost = member.find('cost').tag
        product_head.append(cost)
        weight = member.find('weight').tag
        product_head.append(weight)
        csvwriter.writerow(product_head)
        count = count + 1
    id = member.find('id').text
    product.append(id)
    name = member.find('productName').text
    product.append(name)
    cost = member.find('cost').text
    product.append(cost)
    weight = member.find('weight').text
    product.append(weight)
    csvwriter.writerow(product)
product_data.close()

