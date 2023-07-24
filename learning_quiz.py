import json
import random


class Quiz:
    def __init__(self, filename):
        self.filename = filename
        self.questions = []

    def load_questions(self):
        try:
            with open(self.filename, "r") as file:
                self.questions = json.load(file)
        except FileNotFoundError:
            self.questions = []

    def run_quiz(self):
        random.shuffle(self.questions)
        score = 0

        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question['question']}")
            random.shuffle(question["options"])
            for j, option in enumerate(question["options"], 1):
                print(f"{j}. {option}")

            user_answer = input("Enter your answer: ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(
                question["options"]
            ):
                if question["options"][int(user_answer) - 1] == question["answer"]:
                    print("Correct answer!")
                    score += 1
                else:
                    print(
                        f"Incorrect answer! The correct answer is {question['answer']}"
                    )
            else:
                print("Invalid input. Skipping this question.")

            print()

        print(f"Quiz completed! Your score is {score}/{len(self.questions)}")


quiz = Quiz("test_quiz.json")
quiz.load_questions()

quiz.run_quiz()
