## task 2 – Computational Complexity Analysis (P vs NP)

## overview
This project explores a classroom seating arrangement problem where students must be seated in a single row without placing friends or students from the same city next to each other. It uses this scenario to explain the difference between P and NP problems, comparing brute force and heuristic solution approaches.

## Problem Scenario:

1. Friends cannot sit next to each other (to prevent talking).
2.Students from the same city cannot sit next to each other.

#What is a P Problem?

A P (Polynomial-time) problem is one that can be solved efficiently.
The runtime grows at a manageable rate (e.g., O(n), O(n²), O(n³)).

#Why Checking is Easy (P-like Behavior)

-The teacher scans adjacent students
-Only n−1 pairs need to be checked
-Time complexity: O(n)

#Performance Comparison
| Students | Brute Force Checks | Heuristic Steps | Brute Force Runtime | Heuristic Runtime |
| -------- | ------------------ | --------------- | ------------------- | ----------------- |
| 4        | 24                 | 4               | 0.002 sec           | 0.1 ms            |
| 10       | 3.6 Million        | 10              | 3.6 sec             | 0.5 ms            |
| 15       | 1.3 Trillion       | 15              | 15 days             | 0.8 ms            |
| 20       | 2.4 Quintillion    | 20              | 77,000 years        | 1 ms              |

# how to run 

##Prerequisites

```
# Python 3 required
python --version
```
## Run Brute Force
```
cd Scripts
python Brute-force.py
```
##Run Brute Force
```
cd Scripts
python Brute-force.py
```

##output

###
Brute Force (for 4 students)
<img width="917" height="301" alt="h approach" src="https://github.com/user-attachments/assets/3a1951d6-1633-4c04-959f-9806b018d25c" />


