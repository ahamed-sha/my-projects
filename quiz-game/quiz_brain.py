class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # TODO 3. checking if we're at the end of the quiz

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    # TODO 1. asking the question

    def next_question(self):
        qn = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {qn.text}. (True/False):   ")
        self.check_answer(user_ans, qn.answer)

    # TODO 2. checking if the answer was correct

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1

        else:
            print("You are wrong!")
            print(f"the correct answer is {correct_answer}")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n")
