Overview

(**normalization**)Normalization is a database design technique used to organize data in a database efficiently.
It reduces data redundancy and avoids problems like insert, update, and delete anomalies.
The process is done by dividing a large table into smaller related tables.

Database Schema and Table of  College Club Membership Management

<img width="968" height="406" alt="image" src="https://github.com/user-attachments/assets/1a538586-8750-4c75-b04f-888f6410de13" />



Identify Data Problems from the Table(At least 3 problems)

## Problem 1: Data Rudundancy

--Student data (name,email) is repeated multiple times.
-club data (room,Mentor) is also repeated.

## problem 2: update Anomaly

- If Music Club room chnages, we must update it in many rows.
- Missing even one row causes Wrong data.

## Problem: INsert Anomaly 

-you cannot add a new unless at least one student join it.

**Reasons that Above that is not normalized**

-multiple subjects (Student + club + Membership) are stored in one table.
-Reapeated data exists
-Dependence are not clear
-Cause anomalies like ( insert, update, delete).

** quick start 
```
git clone https://github.com/AashVortex/ST4015CMD-Foundations-of-Computer-Science
cd ST4015CMD-Foundations-of-Computer-Science
```

Unnormalized Form (Initial)

```
data ( StudentID, StudentName, Email, ClubName, ClubRoom, ClubMentor, JoinDate )

```
-- from the above table it is already in 1NF (First normal form )

Second normal form (2NF)

- **Student** ( StudentID , StudentName , Email )
- **Club** ( ClubID , Clubname , ClubRoom , ClubMentor )
- **Membership ( StudenID , ClubID , JoinDate )


-**not** (after coventing the table to second norm form, no transitive dependence remained.Therefore, the tables already satisfy Third Normal Form, and no further decomposition was required)


-**Usage Instructions**

STEP 1: Create unnormalized Table

```bash
CREATE TABLE DATA (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    StudentID INT,
    StudentName VARCHAR(50),
    Email VARCHAR(50),
    ClubName VARCHAR(50),
    ClubRoom VARCHAR(50),
    ClubMentor VARCHAR(50),
    JoinDate DATE
);
INSERT INTO DATA (StudentID, StudentName, Email, ClubName, ClubRoom, ClubMentor, JoinDate) VALUES
(1, 'Asha', 'asha@email.com', 'Music Club', 'R101', 'Mr. Raman', '2024-01-10'),
(2, 'Bikash', 'bikash@email.com', 'Sports Club', 'R202', 'Ms. Sita', '2024-01-12'),
(1, 'Asha', 'asha@email.com', 'Sports Club', 'R202', 'Ms. Sita', '2024-01-15'),
(3, 'Nisha', 'nisha@email.com', 'Music Club', 'R101', 'Mr. Raman', '2024-01-20'),
(4, 'Rohan', 'rohan@email.com', 'Drama Club', 'R303', 'Mr. Kiran', '2024-01-18'),
(5, 'Suman', 'suman@email.com', 'Music Club', 'R101', 'Mr. Raman', '2024-01-22'),
(2, 'Bikash', 'bikash@email.com', 'Drama Club', 'R303', 'Mr. Kiran', '2024-01-25'),
(6, 'Pooja', 'pooja@email.com', 'Sports Club', 'R202', 'Ms. Sita', '2024-01-27'),
(3, 'Nisha', 'nisha@email.com', 'Coding Club', 'Lab1', 'Mr. Anil', '2024-01-28'),
(7, 'Aman', 'aman@email.com', 'Coding Club', 'Lab1', 'Mr. Anil', '2024-01-30');
```

### Step 2: Apply normalizatiom
(See `NeoAash_database.sql` for complete normalization step)

##Inseting a new student on the table (Student)

```bash
INSERT INTO Student VALUES
     (8,'Aashish','aashish@email.com');
```

-- Inserting a new Club into the Club table

```bash
INSERT INTO Club VALUES
     (5,'hacking club','R699','ms.piya');
```

## Verification & Testing
**Test case:1**
```sql
SELECT * FROM  Student;
```
**Expected Output:**
```
+-----------+-------------+-------------------+
| StudentID | Studentname | Email             |
+-----------+-------------+-------------------+
|         1 | Asha        | asha@email,com    |
|         2 | Bikash      | bikash@email.com  |
|         3 | Nisha       | nisha@email.com   |
|         4 | Rohan       | rohan@email.com   |
|         5 | Suman       | suman@email.com   |
|         6 | Pooja       | pooja@email.com   |
|         7 | Aman        | aman@email.com    |
|         8 | Aashish     | aashish@email.com |
+-----------+-------------+-------------------+
```

## Test case:2 
```Sql
SELECT * FROM Club;
```
**Expected Output:**
```
+--------+--------------+----------+------------+
| ClubID | Clubname     | ClubRoom | ClubMentor |
+--------+--------------+----------+------------+
|      1 | music club   | R101     | mr.Raman   |
|      2 | sports club  | R202     | ms. sita   |
|      3 | drama club   | R303     | mr. kiran  |
|      4 | coding club  | lab1     | mr. anil   |
|      5 | hacking club | R699     | ms.piya    |
+--------+--------------+----------+------------+
```
## Test case:3 
```sql
SELECT * FROM Memberships;
```
**Expected Output:**
```
+-----------+--------+------------+
| StudentID | ClubID | JoinDate   |
+-----------+--------+------------+
|         1 |      1 | 2024-01-10 |
|         1 |      2 | 2024-01-15 |
|         2 |      2 | 2024-01-12 |
|         2 |      3 | 2024-01-25 |
|         3 |      1 | 2024-01-20 |
|         3 |      4 | 2024-01-28 |
|         4 |      3 | 2024-01-18 |
|         5 |      1 | 2024-01-22 |
|         6 |      2 | 2024-01-27 |
|         7 |      4 | 2024-01-30 |
+-----------+--------+------------+
```
## Test case 4: Join operation between (Student Table , Club table , Membership table) displaying the Student Name , Club name , join date

```sql
SELECT s.StudentName, c.ClubName, m.JoinDate
FROM Membership m
JOIN Student s ON m.StudentID = s.StudentID
JOIN Club c ON m.ClubID = c.ClubID;
```
**Expected Output:**
```
+-------------+-------------+------------+
| StudentName | ClubName    | JoinDate   |
+-------------+-------------+------------+
| Asha        | music club  | 2024-01-10 |
| Nisha       | music club  | 2024-01-20 |
| Suman       | music club  | 2024-01-22 |
| Bikash      | sports club | 2024-01-12 |
| Asha        | sports club | 2024-01-15 |
| Pooja       | sports club | 2024-01-27 |
| Rohan       | drama club  | 2024-01-18 |
| Bikash      | drama club  | 2024-01-25 |
| Nisha       | coding club | 2024-01-28 |
| Aman        | coding club | 2024-01-30 |
+-------------+-------------+------------+
```






