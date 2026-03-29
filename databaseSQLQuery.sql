USE student_db;
SELECT * FROM students;
drop table students;
CREATE TABLE students (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
);
INSERT INTO students (name, age, course) VALUES ('Surekha', 21, 'Computer Science');
INSERT INTO students (name, age, course) VALUES ('Ravi', 22, 'Electronics');
INSERT INTO students (name, age, course) VALUES ('Priya', 20, 'Information Technology');
INSERT INTO students (name, age, course) VALUES ('Kiran', 23, 'Mechanical');
INSERT INTO students (name, age, course) VALUES ('Anjali', 21, 'Data Science');