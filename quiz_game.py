

questions = [
    {
        "prompt": "What is the Capital of South Korea?",
        "options": ["A. Seoul", "B. Buson", "C. Incheon", "D. Gimpo"],
        "answer": "A"
    },
    {
        "prompt": "What language is primarily spoken in South Korea?",
        "options": ["A. English", "B. Mandarin", "C. Korean", "D. Japanese"],
        "answer": "C"
    },
    {
        "prompt": "How many hours per year do students study in upper secondary school?",
        "options": ["A. 672 hours", "B. 544 hours", "C. 767 hours", "D. 517 hours"],
        "answer": "B"
    },
    {
        "prompt": "What is the name of the convention help in LA to celebrate Korean culture?",
        "options": ["A. Comic-Con", "B. VidCon", "C. AnimeCon", "D. KCon"],
        "answer": "D"
    }
]
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, D): ").upper()
        if answer == question["answer"]:
            print("Correct \n")
            score += 1
        else:
            print("Incorrect. The correct answer is", question["answer"], "\n")

    print(f"You got {score} out of {len(questions)} questions correct.")

run_quiz(questions)