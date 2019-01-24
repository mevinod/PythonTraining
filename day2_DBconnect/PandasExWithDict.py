import pandas as sp


try:
    print("Define a list : ")
    data = [[10,"Vinod", 74], [11, "Keerthi", 68], [12, "Vijay", 94]]
    print(data)

    try:
        df = sp.DataFrame(data, columns=['ID', 'Name', 'Percent'])
        print('Converting into DataFrame')
        print(df)
    except Exception as e:
        print('Something went wrong while converting to frames', e)

except Exception as e:
    print('Oohhoo.. something went wrong', e)

"""
data = {
'ID' : [10, 11, 12],
'Name' : ['A', 'B', 'C']
}

print(data)
df=sp.DataFrame(data)
print(data)
"""