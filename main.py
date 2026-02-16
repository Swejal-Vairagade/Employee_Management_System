from db_config import create_connection
def add_employee(name, department, salary, hire_date):
    conn = create_connection()

    if conn is None:
        print("Database Connection Working!")
        return
    
    cursor = conn.cursor()

    query="""INSERT INTO employees(name, department, salary, hire_date)
    VALUES (%s, %s, %s, %s)"""

    values=(name, department, salary, hire_date)

    try:
        cursor.execute(query, values)
        conn.commit()
        print("Employee added successfully!")
    except Exception as e:
        print("ERROR inserting employee:", e)
    finally:
        cursor.close()
        conn.close()

add_employee("Rahul Sharma","IT",55000.55,"2024-01-15")                 