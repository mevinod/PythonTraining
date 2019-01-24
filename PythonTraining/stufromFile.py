#Create a file
fileObj = open ('sudent.txt',"w+") #w+ for creating a file
print(fileObj)

#print (fileObj.read()) or fileObj.seek(0)
#@fileObj.close()

'''myList = fileObj.readlines()

for data in myList:
    print(data)
'''
print (fileObj.read())

print("Writable?", fileObj.writable())

fileObj.close()
