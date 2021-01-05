import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
PADX = 100
PADY = 40
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 224
CHECK_MARK = "✔"
reps = 0
work_reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", foreground = GREEN)
    canvas.itemconfig(time_remaining_text,text="00:00")
    check_marks_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        time = long_break_sec
        timer_label.config(text="Long Break", foreground = RED)
    if reps % 2 == 0:
        time = short_break_sec
        timer_label.config(text="Short Break", foreground = PINK)
    else:
        time = work_sec
        timer_label.config(text="Work", foreground=GREEN)

    count_down(time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_remaining_text , text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        check_marks = ""
        completed_work_reps = math.floor(reps / 2)
        for work_reps in range(completed_work_reps):
            check_marks.append(CHECK_MARK)
        check_marks_label.config(text=check_marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pomodoro Timer")
window.config(padx = PADX, pady = PADY, bg = YELLOW)
canvas = Canvas(width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
time_remaining_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row = 1, column = 1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row = 2, column = 0)


reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row = 2, column = 2)


# Labels
timer_label = Label(text="Timer", foreground = GREEN, background = YELLOW, font = (FONT_NAME, 35, "bold"))
timer_label.grid(row = 0, column = 1)

check_marks_label = Label( fg = GREEN, bg = YELLOW)
check_marks_label.grid(row = 4, column = 1)

window.mainloop()