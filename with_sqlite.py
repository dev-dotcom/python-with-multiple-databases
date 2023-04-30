import sqlite3

conn = sqlite3.connect('demo.db')
cur = conn.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS employees(Id INTEGER,Name TEXT, Designation TEXT, Branch TEXT)
""")


# cur.execute("""
#     INSERT INTO employees(Id,Name,Designation,Branch) 
#     VALUES 
#     (1,"Michael Scott","Regional Manager","Scranton"),
#     (2,"Dwight K. Schrute","Sales Person & Assistant to the Regional Manager","Scranton"),
#     (3,"Jim Halpert","Sales Person","Scranton"),
#     (4,"Pam Beesly","Sales Person","Scranton"),
#     (5,"Kevin Malone","Accountant","Scranton"),
#     (6,"Oscar Martinez","Accountant","Scranton"),
#     (7,"Angela Martin","Accountant","Scranton"),
#     (8,"Phyllis Vance","Sales Person","Scranton"),
#     (9,"Stanley Hudson","Sales Person","Scranton"),
#     (10,"Andy Bernard","Sales Person","Scranton"),
#     (11,"Toby Flenderson","Human Resources","Scranton"),
#     (12,"Ryan Howard","Temp","Scranton"),
#     (13,"Kelly Kapoor","Customer Service Representative","Scranton"),
#     (14,"Darryl Philbin","Warehouse Manager","Scranton"),
#     (15,"Creed Braton","Quality Assurance","Scranton"),
#     (16,"Meredith Palmer","Purchasing/Supplier Relations","Scranton"),
#     (17,"Erin Hanon","Receptionist","Scranton")
# """)

# cur.execute("""
#     UPDATE employees
#     SET Designation="Sales Person"
#     WHERE Id=2
# """)

# cur.execute("""
#     DELETE FROM employees
#     WHERE Id=17
# """)

# cur.execute("""
#     INSERT INTO employees(Id,Name,Designation,Branch) VALUES(17,"Erin Hanon","Receptionist","Scranton")
# """)
conn.commit()
cur.execute("""
    SELECT * FROM employees
""")
data = cur.fetchall()
for i in data:
    print(i)
cur.close()
conn.close()