import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_score = {name: random.randint(60, 100) for name in names}

print(student_score)

best_students = {student: score for student, score in student_score.items() if score > 80}

print(best_students)