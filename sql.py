import sqlite3
import random

connection = sqlite3.connect("student.db")

## Create a db 
cursor = connection.cursor()

table_info = """ 
Create table STUDENT_table(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""


cursor.execute(table_info)

# Sample data lists
names = ['Alex', 'Emma', 'Noah', 'Sophia', 'Liam', 'Olivia', 'Lucas', 'Ava', 'Mason', 'Isabella',
         'Nathan', 'Maya', 'Ethan', 'Zoe', 'Ryan', 'Sarah', 'Jack', 'Lily', 'Daniel', 'Grace',
         'David', 'Anna', 'Michael', 'Emily', 'James']

courses = ['Data Science', 'DEVOPS', 'Web Development', 'Cloud Computing', 'Machine Learning', 
          'Cybersecurity', 'Mobile Development', 'Database Administration', 'UI/UX Design']

sections = ['A', 'B', 'C']

# Generate and insert 50 records
for i in range(50):
    # Create random student data
    name = f"{random.choice(names)} {chr(65 + random.randint(0, 25))}"  # Add a random last initial
    course = random.choice(courses)
    section = random.choice(sections)
    marks = random.randint(35, 100)  # Marks between 35 and 100
    
    # Insert record
    cursor.execute('''INSERT INTO STUDENT_table (NAME, CLASS, SECTION, MARKS) 
                     VALUES (?, ?, ?, ?)''', (name, course, section, marks))
    
# Commit the changes and print confirmation
connection.commit()
print("Successfully inserted 50 records")

# Let's verify by selecting and displaying a few records
cursor.execute('''SELECT * FROM STUDENT_table''')
print("\nFirst 5 records as sample:")
for row in cursor.fetchall():
    print(row)

connection.commit()
connection.close()
