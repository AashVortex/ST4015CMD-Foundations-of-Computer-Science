import itertools

# List of students
students = ["A", "B", "C", "D"]

# Function to check if arrangement is valid
def is_valid(arrangement):
    
    # Example condition 1: A cannot sit next to B
    for i in range(len(arrangement) - 1):
        if arrangement[i] == "A" and arrangement[i+1] == "B":
            return False
        if arrangement[i] == "B" and arrangement[i+1] == "A":
            return False

    # Example condition 2: C must sit before D
    if arrangement.index("C") > arrangement.index("D"):
        return False

    return True


# Brute force: generate all permutations
valid_arrangements = []

for perm in itertools.permutations(students):
    if is_valid(perm):
        valid_arrangements.append(perm)

# Print results
print("Valid Seating Arrangements:")
for arr in valid_arrangements:
    print(arr)

print("Total Valid Arrangements:", len(valid_arrangements))