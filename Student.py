class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [
    Student("Ali", 75),
    Student("Samin", 92),
    Student("Areesha", 45)
]
def top_scorer(students):
    highest = students[0]

    for student in students:
        if student.score > highest.score:
            highest = student

    return highest


print("Students with scores above 50:")

for student in students:
    if student.score > 50:
        print(student.name, "-", student.score)

top = top_scorer(students)

print("\nTop Scorer:")
print(top.name, "-", top.score)
