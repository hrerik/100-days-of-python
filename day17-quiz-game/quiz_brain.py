class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.num_questions = len(self.question_list)

    def still_has_questions(self):
        return self.question_number < self.num_questions

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}) {question.text} (True/False)?\n>")
        self.check_answer(ans, question.answer)

    def check_answer(self, correct_answer, question_answer):
        if correct_answer.lower() == question_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")
            print(f"The correct answer was {question_answer}")

        print(f"Your score is {self.score}/{self.question_number}.\n")
