# Employee Management System (Python + MySQL)

A simple menu-driven Employee Management System built using Python and MySQL that performs full CRUD operations and demonstrates Software Development Life Cycle (SDLC) phases.

## Features
- Add Employee
- View Employees
- Update Employee
- Delete Employee
- Menu Driven Interface
- MySQL Database Integration
- Clean Database Connection Handling(show_message parameter)

## Tech Stack
- Python
- MySQL
- mysql-connector-python
- Git & GitHub
- VS Code

## Database Structure

Table: employees

emp_id (INT, AUTO_INCREMENT, PRIMARY KEY)  
name (VARCHAR)  
salary (FLOAT)  

# Software Development Life Cycle (SDLC Phases)

## Phase 1 - Requirement Analysis
- Need a system to manage employee records
- Must support CRUD operations
- Should connect Python with MySQL
- Menu driven interface required

## Phase 2 — System Design
- Designed MySQL database
- Created employees table
- Used AUTO_INCREMENT for emp_id
- Created project folder structure

#### Files:
- main.py
- db_config.py

## Phase 3 — Database Connection
- Connected Python to MySQL
- Created reusable create_connection() function
- Added optional show_message parameter

## Phase 4 — Create Operation
- Insert employee into database
- Accept user input
- Commit transaction
- Success message displayed

## Phase 5 — Read Operation
- Fetch all records
- Display in formatted output
- Handle empty table case

## Phase 6 — Update Operation
- Update employee using emp_id
- Modify name and salary
- Commit changes
- Success message shown

## Phase 7 — Delete Operation
- Delete employee using emp_id
- Confirmation message
- Database updated

## Phase 8 — Menu Driven System
- Implemented interactive menu
- Loop based execution
- Options:
   - Add Employee
   - View Employees
   - Update Employee
   - Delete Employee
   - Exit
- Improved DB connection using show_message parameter

## Project Structure

employee_management_system  
│  
├── main.py  
├── db_config.py  
├── .gitignore  
└── README.md  

## How to run:
#### Install dependency:
- pip install mysql-connector-python  
#### Run project:
- python main.py  
