import html

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.goodcount = 0

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        self.current_q = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.current_q.text)}"

    def check_answer(self, guess):
        if guess.lower() == self.current_q.answer.lower():
            self.goodcount += 1
            return True
        else:
            return False