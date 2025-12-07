grades = {"John": "A", "Sara": "B", "Musa": "A"}
inverted = {}

for student, grade in grades.items():
    if grade in inverted:
        inverted[grade].append(student)
    else:
        inverted[grade] = [student]
print(inverted)
