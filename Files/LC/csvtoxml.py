import os
import csv

csvFile = os.path.join('C:/Users/ssubra029c/Documents/CTS/QA2QE/Python/Files', 'product_1.csv')
xmlFile = os.path.join('C:/Users/ssubra029c/Documents/CTS/QA2QE/Python/Files', 'product_1.xml')

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
# there must be only one top-level tag
xmlData.write('<productList>' + "\n")

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else:
        xmlData.write('<product>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</product>' + "\n")

    rowNum += 1

xmlData.write('</productList>' + "\n")
xmlData.close()

