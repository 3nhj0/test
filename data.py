



import mysql.connector

# Establish a connection
conn = mysql.connector.connect(
    host='localhost',  # Replace with your MySQL host
    user='enhj0',
    password='password',
    database='NS356'
)

# Create a cursor object
cursor = conn.cursor()

insert_query = "INSERT INTO identity (name ,code) VALUES (%s, %s)"

with open('table1.txt', 'r', encoding='utf-8') as file1:
    for line in file1:

        if len(line) > 2:
            line = line.split(',')
            name = line[0]
            code = line[1]

            values = (str(name.strip()), str(code.strip()))
            # print(values)
            cursor.execute(insert_query, values)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

