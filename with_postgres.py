import psycopg2

conn = psycopg2.connect(
    database="Demo",
    host="localhost",
    user="postgres",
    password="devict444",
    port="5432"
)

cur = conn.cursor()


# cur.execute("""
#     INSERT INTO public."Employees"("Id","Name","Designation","Branch") 
#     VALUES
#     (4,'Pam Beesly','Sales Person','Scranton'),
#     (5,'Kevin Malone','Accountant','Scranton'),
#     (6,'Oscar Martinez','Accountant','Scranton'),
#     (7,'Angela Martin','Accountant','Scranton'),
#     (8,'Phyllis Vance','Sales Person','Scranton'),
#     (9,'Stanley Hudson','Sales Person','Scranton'),
#     (10,'Andy Bernard','Sales Person','Scranton'),
#     (11,'Toby Flenderson','Human Resources','Scranton'),
#     (12,'Ryan Howard','Temp','Scranton'),
#     (13,'Kelly Kapoor','Customer Service Representative','Scranton'),
#     (14,'Darryl Philbin','Warehouse Manager','Scranton'),
#     (15,'Creed Braton','Quality Assurance','Scranton'),
#     (16,'Meredith Palmer','Purchasing/Supplier Relations','Scranton'),
    # (17,'Erin Hanon','Receptionist','Scranton')
# """)

# data = cur.fetchone()
# print(data)

# cur.execute("""
# SELECT * FROM public."Employees"
# """)

# data = cur.fetchall()
# cur.close()
# for i in data:
#     print(i)

# cur.execute("""
#     UPDATE public."Employees"
# 	SET "Designation"='Sales Person & Assistant to the Regional Manager'
# 	WHERE "Id" = 2;
# """)

# cur.execute("""
# DELETE FROM public."Employees"
# 	WHERE "Id"=17
# """)
conn.commit()
cur.close()