import sqlite3
try:
    conn = sqlite3.connect('demoDB.db') #Connection to database
    c = conn.cursor() #Create cursor which interacts with database connection
    c.execute("""CREATE TABLE IF NOT EXISTS employee(
    EMP_ID integer,
    EMP_Name text,
    EMP_sal integer)
    """)
    print('Table Employee is created')
    conn.commit()#Commmit the changes to the connected database

    try:
        conn.execute("""INSERT INTO employee (EMP_ID,EMP_Name,EMP_sal) 
              VALUES (500, 'Paul', 3200),
              (78, 'Keith', 35400),
              (98, 'Kath', 55110),
              (9, 'Keith', 35400)
              """)
        print('Insertion is successfully')
        conn.commit()
    except sqlite3.Error as e:
        print('Something went wrong while inserting, please try again', e)

    try:
        c.execute('Select * from employee')
        print(c.fetchall())
    except sqlite3.Error as e:
        print('Some issue in fetching the result', e)

    try:
        c.execute("UPDATE employee set EMP_ID = 1 where EMP_Name = 'Paul'")
        print('Updated successfully')
        conn.commit()
    except sqlite3.Error as e:
        print('Failed to update the record', e)

    try:
        c.execute('Select * from employee')
        print(c.fetchall())
    except sqlite3.Error as e:
        print('Some issue in fetching the result', e)


    conn.close() #Close connection
except ConnectionError as e:
    print('There is some issue in connecting to database, please try again', e)
except NameError as e:
    print('Some connection param is wrong? Please check')

