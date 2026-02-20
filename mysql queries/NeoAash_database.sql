-- cryzen_ash Database Normalization Lab
CREATED DATABASE NeoAash;

USE NeoAash;


-- Part A: Unnormalized Table
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
