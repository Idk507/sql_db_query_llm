import sqlite3
import random

connection = sqlite3.connect("student.db")

## Create a db 
cursor = connection.cursor()

# Let's verify by selecting and displaying a few records
cursor.execute('''SELECT * FROM STUDENT_table''')
print("\nFirst 5 records as sample:")
for row in cursor.fetchall():
    print(row)
connection.commit()
connection.close()