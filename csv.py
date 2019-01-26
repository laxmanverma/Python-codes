import csv

#   Modifying existing rows of people.csv
row = ['2', ' Marie', ' California']

with open('people.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    lines = list(reader)
    lines[2] = row

with open('people.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()
"""
SN, Name, City
1, John, Washington
2, Marie, California
3, Brad, Texas
"""

#   Appending new rows to people.csv file
row = ['4', ' Danny', ' New York']

with open('people1.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()
"""
SN, Name, City
1, John, Washington
2, Marie, California
3, Brad, Texas
4, Danny, New York
"""

#   Write a python list into person.csv file
csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]

with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()
"""
Person,Age
Peter,22
Jasmine,21
Sam,24
"""

#   Write into person1.csv file
person = [['SN', 'Person', 'DOB'],
['1', 'John', '18/1/1997'],
['2', 'Marie','19/2/1998'],
['3', 'Simon','20/3/1999'],
['4', 'Erik', '21/4/2000'],
['5', 'Ana', '22/5/2001']]

csv.register_dialect('myDialect',
quoting=csv.QUOTE_ALL,
skipinitialspace=True)

with open('person1.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in person:
        writer.writerow(row)

f.close()
"""
"SN","Person","DOB"
"1","John","18/1/1997"
"2","Marie","19/2/1998"
"3","Simon","20/3/1999"
"4","Erik","21/4/2000"
"5","Ana","22/5/2001"
"""

#   Writing with custom delimiter as pipe(|)
person = [['SN', 'Person', 'DOB'],
['1', 'John', '18/1/1997'],
['2', 'Marie','19/2/1998'],
['3', 'Simon','20/3/1999'],
['4', 'Erik', '21/4/2000'],
['5', 'Ana', '22/5/2001']]

csv.register_dialect('myDialect',
delimiter = '|',
quoting=csv.QUOTE_NONE,
skipinitialspace=True)

with open('dob.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in person:
        writer.writerow(row)

f.close()
"""
SN|Person|DOB
1|John|18/1/1997
2|Marie|19/2/1998
3|Simon|20/3/1999
4|Erik|21/4/2000
5|Ana|22/5/2001
"""

#   Writing csv file using a lineterminator
csvData = [['Fruit', 'Quantity'], ['Apple', '5'], ['Orange', '7'], ['Mango', '8']]

csv.register_dialect('myDialect', delimiter = '|', lineterminator = '\r\n\r\n')

with open('lineterminator.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    writer.writerows(csvData)

f.close()
"""
Fruit|Quantity
Apple|5
Orange|7
Mango|8
"""

#   Writing CSV FIle with quotechars
csvData = [['SN', 'Items'], ['1', 'Pen'], ['2', 'Book'], ['3', 'Copy']]

csv.register_dialect('myDialect',
delimiter = '|',
quotechar = '"',
quoting=csv.QUOTE_ALL,
skipinitialspace=True)

with open('quotechars.csv', 'w') as csvFile:
    writer = csv.writer(csvFile, dialect='myDialect')
    writer.writerows(csvData)

print("writing completed")

csvFile.close()
"""
"SN"|"Items"
"1"|"Pen"
"2"|"Book"
"3"|"Copy"
"""

#   Writing dictionary into peak.csv file
data = [{'mountain' : 'Everest', 'height': '8848'},
      {'mountain' : 'K2 ', 'height': '8611'},
      {'mountain' : 'Kanchenjunga', 'height': '8586'}]

with open('peak.csv', 'w') as csvFile:
    fields = ['mountain', 'height']
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

print("writing completed")

csvFile.close()
"""
mountain,height
Everest,8848
K2,8611
Kangchenjunga,8586
"""

#   Writing dictionary into grade.csv file with custom dialects
csv.register_dialect('myDialect', delimiter = '|', quoting=csv.QUOTE_ALL)

with open('grade.csv', 'w') as csvfile:
    fieldnames = ['Name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect="myDialect")
    writer.writeheader()
    writer.writerows([{'Grade': 'B', 'Name': 'Alex'},
                 {'Grade': 'A', 'Name': 'Bin'},
                 {'Grade': 'C', 'Name': 'Tom'}])

print("writing completed")
"""
"Name"|"Grade"
"Alex"|"B"
"Bin"|"A"
"Tom"|"C"
"""