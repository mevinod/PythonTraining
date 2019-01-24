'''class Person:
    def __init__(self):
        
        print('Our Class is created')

    def __del__(self):
        print('Class Objs are destroyed')

    def setFullName (self,fName,laName):
        self.fName=fName
        self.laName=laName
    def printFullName(self):
        print(self.fName, " ", self.laName)

PersonName = Person()
PersonName.setFullName('Vinod','Bal')
PersonName.printFullName()
PersonName.__del__()'''

a=0
b=0
try:
    print(a/b)
except ZeroDivisionError as e:
    print(e)

try:
    print(c)
except NameError as e:
    print(e)

myList = [12,34,54,54]
try:
    print(myList[5])
    print(k)
except IndexError as e:
    print(e)
finally:
    print('I am done')
