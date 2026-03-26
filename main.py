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

def view_employees():
    conn=create_connection()

    if conn is None:
        print("connection failed")
        return
    
    cursor=conn.cursor()
    query="SELECT * FROM employees"

    try:
        cursor.execute(query)
        records = cursor.fetchall()

        print("\n Employee Records")
        print("-" * 60)

        if not records:
            print("No employee found.")
        else:
            for row in records:
                print(row)
    except Exception as e:
        print("error fetching data:", e)

    finally:
        cursor.close()
        conn.close()

def update_employee(emp_id, department, salary):
    conn= create_connection()

    if conn is None:
        print("Connection failed") 
        return
    
    cursor =conn.cursor()

    query ="""
    UPDATE employees
    SET department = %s, salary=%s
    WHERE emp_id =%s"""

    values =(department,salary,emp_id)  

    try:
        cursor.execute(query, values)
        conn.commit()

        if cursor.rowcount>0:
            print("Employee updated successfully!")
        else:
            print("EMployee id not found")
    except Exception as e:
        print("Error updating employeee:", e)
    finally:
        cursor.close()
        conn.close()  

def delete_employee(emp_id):
    conn=create_connection()

    if conn is None:
        print("Connection failed")
        return
    cursor=conn.cursor()
    query="DELETE from employees WHERE emp_id = %s"
    try:
        cursor.execute(query,(emp_id,))
        conn.commit()
        if cursor.rowcount>0:
            print("Employee deleted successfully!")
        else:
            print("Employee id not found.")
    except Exception as e:
        print("Error deleting employee=", e)
    finally:
        cursor.close()
        conn.close()                

def menu():
    while True:
        print("\n==== Employee Management System ====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice =="1":
            name = input("Enter name: ")
            dept = input("Enter Department: ")
            salary = float(input("Enter Salary: "))
            hire_date =input("Enter hire date (YY-MM-DD): ")

            add_employee(name, dept, salary, hire_date)

        elif choice == "2":
            view_employees()

        elif choice == "3":
            emp_id = int(input("Enter employee id to update: "))
            dept = input("Enter new department: ")
            salary = float(input("Enter new salary: "))

            update_employee(emp_id,dept,salary)

        elif choice == "4":
            emp_id =int(input("Enter employee ID to delete: ")) 
            delete_employee(emp_id)

        elif choice == "5":
            print("Exiting system.Goodbye!")
            break

        else:
            print("Invalid choice.Try Again.")       

if __name__ == "__main__":
    menu()   


