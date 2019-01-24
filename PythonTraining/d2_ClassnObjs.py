class Person:
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
PersonName.__del__()
