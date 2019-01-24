#Create a file
fileObj = open ('demo.txt',"w+") #w+ for creating a file
print(fileObj)

for i in range(10):
    fileObj.write("This is line %d\r\n" % (i+1))

fileObj.close()
