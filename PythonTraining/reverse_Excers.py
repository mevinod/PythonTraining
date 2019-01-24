#Create a file

fileObj = open ('fun.txt', "w+")
print(fileObj)

fileObj = open ('fun.txt','w')

lst = ['Hi']
fileObj.writelines(lst)

print(lst)



fileObj.close()
