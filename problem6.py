import mysql.connector
from mysql.connector import Error
import random  # Ensure this line is added to import the random module

def insert_data():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Assuming user is 'root'
            password="Mouni7788",  # Your MySQL password
            database="query"  # Your MySQL database name
        )
        if conn.is_connected():
            print("Connected to MySQL database")
            cursor = conn.cursor()

            # Insert data into R1
            R1_data = [(i, 5) for i in range(1, 1001)] + [(i, 7) for i in range(1001, 2001)] + [(2001, 2002)]
            cursor.executemany("INSERT INTO R1 (i, x) VALUES (%s, %s)", R1_data)

            # Insert data into R2
            R2_data = [(5, i) for i in range(1, 1001)] + [(7, i) for i in range(1001, 2001)] + [(2002, 8)]
            cursor.executemany("INSERT INTO R2 (y, j) VALUES (%s, %s)", R2_data)

            # Insert data into R3 with random values
            R3_data = [(random.randint(2002, 3000), random.randint(1, 3000)) for _ in range(2000)] + [(8, 30)]
            cursor.executemany("INSERT INTO R3 (x, z) VALUES (%s, %s)", R3_data)

            # Commit the changes
            conn.commit()
            print("Data inserted successfully")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

# Run the function to insert data
insert_data()
