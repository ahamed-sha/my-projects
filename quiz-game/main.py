from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    qn_text = item["text"]
    qn_answer = item["answer"]
    question = Question(qn_text, qn_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("you've completed the quiz")
print(f"your final score was : {quiz.score} / {quiz.question_number}")
