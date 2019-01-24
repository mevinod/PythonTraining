import pandas as sp


try:
    print("Define a list : ")
    myList = [[2, 1], [3, 5], [6, 8]]
    print(myList)

    try:
        df = sp.DataFrame(myList)
        print('Converting into DataFrame')
        print(df)
    except Exception as e:
        print('Something went wrong while converting to frames', e)

except Exception as e:
    print('Oohhoo.. something went wrong', e)


