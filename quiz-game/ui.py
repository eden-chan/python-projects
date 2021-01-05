from tkinter import *
THEME_COLOR = "#11AABB"
class QuizInterface:
    def __init__(self):
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(height = 600, width = 340)
        self.window.config(padx = 20, pady = 20, background = "#11AABB")
        self.score_label = Label(text=f"Score: {self.score}", background = THEME_COLOR, foreground = "white")
        self.score_label.grid(row=0, column = 1)
        self.canvas = Canvas()
        self.canvas.grid(row = 1, column = 0, columnspan= 2, pady= 50)
        self.question_text = self.canvas.create_text(100, 130, text = "TEXT", fill = "white", font=("Arial", 20, "italic"))


        self.window.mainloop()

    def change_question(self, new_question_text):
        self.canvas.itemconfig(self.question_text, text=new_question_text)

