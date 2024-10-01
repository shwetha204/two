quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is primarily used for web development?",
        "options": ["A) Python", "B) JavaScript", "C) C++", "D) Java"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "C"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["A) Nikola Tesla", "B) Albert Einstein", "C) Isaac Newton", "D) Galileo Galilei"],
        "answer": "B"
    }
]

# Function to ask questions and collect answers
def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for index, question in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {question['question']}")
        for option in question["options"]:
            print(option)

        # Get the user's answer
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        # Check if the answer is correct
        if user_answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")

    # Provide feedback on performance
    print(f"Quiz completed! Your score: {score}/{total_questions}")
    print(f"Percentage: {(score / total_questions) * 100:.2f}%")

# Run the quiz
if __name__ == "__main__":
    print("Welcome to the Quiz!")
    run_quiz(quiz_questions)
