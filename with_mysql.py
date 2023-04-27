import mysql.connector

from mysql import connector

try:
    conn = mysql.connector.connect(
    user = 'root',
    password = "",
    host = "localhost",
    port = 3306,
   database = "Enterprise"
    )
    if conn.is_connected():
        print("Connected")

except Exception as e:
    print("Not connected!",e)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE Enterprise")
print("Database Created")

cursor.execute("USE Enterprise")

cursor.execute("""CREATE TABLE employees(
    emp_No INT PRIMARY KEY,
    emp_Name VARCHAR(100) NOT NULL,
    account VARCHAR(100) NOT NULL,
    status VARCHAR(100) NOT NULL
)""")

query = """INSERT INTO employees(emp_No,emp_Name,account,status) VALUES
    (20372893,"Dev Faldu","Credit One Bank","billable"),
    (28408371,"Jayesh parmar","Mastercard","billable"),
    (22834701,"Deep Sarkar","Visa","Free pool"),
    (20382053,"Mohit Chauhan","53 Processing Ltd","Non-billable")"""
try:    
    cursor.execute(query)
    conn.commit()
    print("Query executed successfully")

except Exception as e:
    conn.rollback()
    print("Query did not executed",e)

finally:
    cursor.close()
    conn.close()
    print("connection closed")