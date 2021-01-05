from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(height = 600, width = 340)
        self.window.config(padx = 20, pady = 20, background = "#11AABB")
        self.score_label = Label(text=f"Score: 0", background = THEME_COLOR, foreground = "white")
        self.score_label.grid(row=0, column = 1)
        self.canvas = Canvas()
        self.canvas.grid(row = 1, column = 0, columnspan= 2, pady= 50)
        self.question_text = self.canvas.create_text(170, 130, width = 280, text = "TEXT", font=("Arial", 20, "italic"))
        self.next_question()
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.right_button = Button(image=true_image, highlightthickness=0, command = self.true_pressed)
        self.right_button.grid(row=2,column=1)
        self.wrong_button = Button(image=false_image, highlightthickness=0, command = self.false_pressed)
        self.wrong_button.grid(row=2, column=0)
        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Final Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.canvas.config(bg="white")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_user_answer_correct = self.quiz.check_answer("True")
        self.give_feedback(is_user_answer_correct)


    def false_pressed(self):
        is_user_answer_correct = self.quiz.check_answer("False")
        self.give_feedback(is_user_answer_correct)


    def give_feedback(self,is_user_answer_correct):
        if is_user_answer_correct:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, self.next_question)


