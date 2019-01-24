#Create a file
fileObj = open ('demo.txt',"w") #w+ for creating a file
lst = ['BigData', 'Feed']
fileObj.writelines(lst)
print(fileObj)


fileObj.close()
