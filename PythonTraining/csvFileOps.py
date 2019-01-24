import csv
myFile = open('tst.csv')
myReader = csv.reader(myFile)

print(myReader)

data=list(myReader)

print(data)
