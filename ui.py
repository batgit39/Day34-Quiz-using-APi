from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)

        self.score_lable = Label(text = "Score: 0", bg = THEME_COLOR, fg = "white")
        self.score_lable.grid(column = 1, row = 0)

        self.canvas = Canvas(width = 300, height = 250, bg = "white")
        self.question = self.canvas.create_text(150, 125, text = "Question", font = ("Arial", 20, "italic"), width = 280, fill = THEME_COLOR)
        self.canvas.grid(column = 0, row = 1, columnspan = 2, pady = 50)

        false_img = PhotoImage(file = "images/false.png")
        self.false_button = Button(image = false_img, highlightthickness = 0, command = self.if_false)
        self.false_button.grid(column = 1, row = 3)


        true_img = PhotoImage(file = "images/true.png")
        self.true_button = Button(image = true_img, highlightthickness = 0, command = self.if_true)
        self.true_button.grid(column = 0, row = 3)

        self.get_next_ques()
        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            self.score_lable.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text = q_text)
        else:
            self.canvas.itemconfig(self.question, text = "You've reached the end of the quiz")
            self.false_button.config(state = "disabled")
            self.true_button.config(state = "disabled")

    def if_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def if_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, ans ):
        if ans:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_ques)
