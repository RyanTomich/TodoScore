import mysql.connector

tasks_db = mysql.connector.connect(host="localhost", user="root", password="Todois14*", database = "todo")
cursor = tasks_db.cursor()

if tasks_db.is_connected():
    db_info = tasks_db.get_server_info()
    print(f'Connected to MySQL server version: {db_info}')
    cursor.execute("select database();")
    record = cursor.fetchone()
    print(f"You're connected to database: {record}")

table = '''CREATE TABLE TASKS(
    CLASS VARCHAR(8),
    ASIGNMENT VARCHAR(60),
    OPEN_DATE DATE,
    DUE_DATE DATE,
    STATUS VARCHAR(13),
    GRADE FLOAT,
    ID INT AUTO_INCREMENT PRIMARY KEY)
'''

# try:
cursor.execute(table)   # creates table, returns error if table exists
print ('hi')
# except mysql.connector.errors.ProgrammingError:
#     pass    # if table exists, continue
