from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class user_interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.title("Quiz")
        self.quiz = quiz_brain
        self.window.iconbitmap("images/logo.ico")
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.quotes = self.canvas.create_text(150, 125, text=self.quiz, width=300, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        #True button
        self.true_image = PhotoImage(file="images/true.png", width=100, height=100)
        self.true_button = Button(image=self.true_image, width=100, height=100, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        #False Button
        self.false_image = PhotoImage(file="images/false.png", width=100, height=100)
        self.false_button = Button(image=self.false_image, width=100, height=100, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        #scoreboard
        self.score = Label(text=f"Score: ", bg=THEME_COLOR, fg="white", highlightthickness=0)
        self.score.grid(row=0, column=1)

        #get_next_question
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions() == False:
            self.canvas.itemconfig(self.quotes, text="You've reached the end of the course")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
        else:
            self.score["text"] = f"Score: {self.quiz.goodcount}"
            self.current_q = self.quiz.next_question()
            self.canvas.itemconfig(self.quotes, text=self.current_q)

    def true_answer(self):
        check = self.quiz.check_answer('true')
        self.feedback(check)

    def false_answer(self):
        check = self.quiz.check_answer('false')
        self.feedback(check)

    def feedback(self, bool: bool):
        if bool == True:
            self.canvas.config(bg="green")
        elif bool == False:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)