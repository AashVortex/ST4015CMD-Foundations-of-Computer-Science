Overview

(**normalization**)Normalization is a database design technique used to organize data in a database efficiently.
It reduces data redundancy and avoids problems like insert, update, and delete anomalies.
The process is done by dividing a large table into smaller related tables.

Database Schema and Table of  College Club Membership Management


<img width="948" height="607" alt="image" src="https://github.com/user-attachments/assets/c8341297-bb0b-4211-877c-304bdc4a795a" />

Identify Data Problems from the Table(At least 3 problems)

## Problem 1: Data Rudundancy

--Student data (name,email) is repeated multiple times.
-club data (room,Mentor) is also repeated.

## problem 2: update Anomaly

- If Music Club room chnages, we must update it in many rows.
- Missing even one row causes Wrong data.

