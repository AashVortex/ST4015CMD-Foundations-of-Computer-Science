# Sample student data
students = [
    {"name": "Alice", "friends": ["Bob", "Charlie"], "city": "CityA"},
    {"name": "Bob", "friends": ["Alice"], "city": "CityB"},
    {"name": "Charlie", "friends": ["Alice"], "city": "CityA"},
    {"name": "David", "friends": [], "city": "CityB"},
    {"name": "Eve", "friends": [], "city": "CityC"},
]

rows = 2
cols = 3

# Initialize empty seating
seating = [[None for _ in range(cols)] for _ in range(rows)]

# Sort students by number of friends (most friends first)
students_sorted = sorted(students, key=lambda s: len(s["friends"]), reverse=True)

def check_conflict(seating, row, col, student):
    """Check if student placement violates heuristic rules"""
    # Check all existing seats
    for r in range(rows):
        for c in range(cols):
            s = seating[r][c]
            if s:
                # Friends should not be adjacent (orthogonal or diagonal)
                if s["name"] in student["friends"] or student["name"] in s["friends"]:
                    if abs(r - row) <= 1 and abs(c - col) <= 1:
                        return True
                # Same city should not be in the same row if possible
                if s["city"] == student["city"] and r == row:
                    return True
    return False

# Heuristic placement
for student in students_sorted:
    placed = False
    # Try to find a seat without conflicts
    for r in range(rows):
        for c in range(cols):
            if seating[r][c] is None and not check_conflict(seating, r, c, student):
                seating[r][c] = student
                placed = True
                break
        if placed:
            break
    # If no perfect seat found, place in first empty seat
    if not placed:
        for r in range(rows):
            for c in range(cols):
                if seating[r][c] is None:
                    seating[r][c] = student
                    placed = True
                    break
            if placed:
                break

# Print final seating arrangement
print("Seating Arrangement:")
for r in seating:
    print([s["name"] if s else None for s in r])