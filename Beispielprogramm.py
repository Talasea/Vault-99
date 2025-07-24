import mysql.connector
from mysql.connector import errorcode, Error
# a)
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = conn.cursor()

    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS schuele")
        print("Database successfully created")
    except mysql.connector.Error as err:
        print(f"Error by creation of database: {err}")

    # Select the newly created database
    conn.database = 'schuele'
# b)
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS schueler(
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(25),
            age INT,
            klasse VARCHAR(25)
        )''')
        print("Table 'schueler' successfully created")
    except mysql.connector.Error as err:
        print(f"Error by creation of table: {err}")
 # c)
    # Insert data into the table
    customerData = [
        ('Max Mustermann', 15, "10B"),
        ('Lisa Musterfrau', 16, "10B"),
        ('Frank Musterkind', 14, "10B")
    ]

    try:
        cursor.executemany('''
        INSERT INTO schueler (name, age, klasse) VALUES (%s, %s, %s)''', customerData)
        conn.commit()
        print("Successfully added values to DB")
    except mysql.connector.Error as err:
        print(f"Error by inserting data: {err}")
    # d)
    def printTable():
        cursor.execute("SELECT * FROM schueler")
        for entry in cursor.fetchall():
            print(entry)
    # e)
    def newAge(id,newAge):
        cursor.execute("UPDATE schueler SET age = %s WHERE id = %s ",(newAge,id))
        conn.commit()
    # f)
    def deleteValueWithID(id):
        cursor.execute("DELETE FROM schueler WHERE id=%s",(id,))
        conn.commit()

    printTable()
    newAge(1,24)
    print("Age changed")
    deleteValueWithID(3)
    print("Deleted value")
    printTable()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("No existing DB")
    else:
        print(err)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

    print("Connection closed")
