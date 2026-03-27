# Employee Management System (Python + MySQL)

A simple menu-driven Employee Management System built using Python and MySQL that performs full CRUD operations and demonstrates Software Development Life Cycle (SDLC) phases.

## Features
- Add Employee
- View Employees
- Update Employee
- Delete Employee
- Menu Driven Interface
- MySQL Database Integration
- Clean Database Connection Handling

## Tech Stack
- Python
- MySQL
- mysql-connector-python
- Git & GitHub

## Database Structure

Table: employees

emp_id (INT, AUTO_INCREMENT, PRIMARY KEY)  
name (VARCHAR)  
salary (FLOAT)  

# Software Development Life Cycle (SDLC)

## Phase 1 — Requirement Analysis
Build Employee Management System with CRUD operations and MySQL connection.

## Phase 2 — System Design
Designed employees table with AUTO_INCREMENT emp_id and project structure.

## Phase 3 — Database Connection
Created reusable create_connection() function in db_config.py.

## Phase 4 — Create Operation
Implemented Add Employee functionality.

## Phase 5 — Read Operation
Implemented View Employees functionality.

## Phase 6 — Update Operation
Implemented Update Employee functionality.

## Phase 7 — Delete Operation
Implemented Delete Employee functionality.

## Phase 8 — Menu Driven System
Implemented menu-driven interface and improved DB connection using show_message parameter.

## Project Structure

employee_management_system  
│  
├── main.py  
├── db_config.py  
├── .gitignore  
└── README.md  

## Run Project

pip install mysql-connector-python  
python main.py  
