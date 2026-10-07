questions = [
    ("What is the capital of India?", "delhi"),
    ("Which language is this project written in?", "python"),
    ("2 + 2 = ?", "4"),
    ("What keyword defines a function in Python?", "def"),
]
score = 0
for q, answer in questions:
    if input(q + " ").strip().lower() == answer:
        print("Correct!"); score += 1
    else: print("Wrong. Answer:", answer)
print(f"Score: {score}/{len(questions)}")
