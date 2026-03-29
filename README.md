# Student Management System

This is a simple project built using Python and SQL Server to manage student records.

## Features
- Add student
- View students
- Update student
- Delete student

## Technologies Used
- Python
- SQL Server
- pyodbc

## Database Setup
Run the following SQL in SQL Server:

```sql
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
);