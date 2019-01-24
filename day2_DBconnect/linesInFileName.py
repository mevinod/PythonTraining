"""  @docString The program is to find number of lines in a file """

FileName = input("Enter the file name: ")
NumberOfLines = 0
try:
    with open(FileName,'r') as f:
        for lines in f:
            NumberOfLines = NumberOfLines + 1
        print("Number of lines in the entered fil", FileName, " is: ", NumberOfLines)
except FileNotFoundError as e:
    print("Enter a valid file: ", e)

