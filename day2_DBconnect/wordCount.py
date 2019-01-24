

EnteredString = input("Enter words: ")
print("The entered string is : ", EnteredString)
Count = 1
try:
    for char in EnteredString:
        if char == " ":
            Count = Count+1
        else:
            pass
    print("Words in entered string is/are: ", Count)
except Exception as e:
    print(e)