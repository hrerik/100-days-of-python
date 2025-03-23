from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data["results"]:
    question_bank.append(Question(data["question"],data["correct_answer"]))

# print(len(question_bank))
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You finished the quiz!!!")
print(f"Your final score was {quiz_brain.score}/{quiz_brain.num_questions}.")
