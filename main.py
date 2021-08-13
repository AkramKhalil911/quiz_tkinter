from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import user_interface
question_bank = []

for data in question_data:
    new_question = Question(data['question'], data['correct_answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
ui = user_interface(quiz)