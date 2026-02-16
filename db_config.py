import mysql.connector

def create_connection():
    try:
        connection =mysql.connector.connect(
            host="localhost",
            user="root",
            password="swej@l098",
            database="employee_db"
        )

        if connection.is_connected():
            print("Connected to MySQL successfully!")
        return connection
    
    except mysql.connector.Error as err:
        print("Error:",err)
        return None