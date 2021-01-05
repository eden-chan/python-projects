from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 50, "bold")
timer = None
# ------------ User Selection
def answer_correct():
    words_to_learn.remove(new_word)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/french_words_to_learn.csv", index = False)
    global timer
    window.after_cancel(timer)
    show_next_word()


def answer_incorrect():
    global timer
    window.after_cancel(timer)
    show_next_word()


def flip_card():
    current_card.itemconfig(language_text_label, text="English")
    current_card.itemconfig(current_card_side, image = card_back_img)
    current_card.itemconfig(current_word, text = new_word['English'])


def show_next_word():
    current_card.itemconfig(language_text_label, text="French")
    current_card.itemconfig(current_card_side, image = card_front_img)
    global new_word
    new_word = random.choice(words_to_learn)
    current_card.itemconfig(current_word, text = new_word['French'])
    global timer
    timer = window.after(5000, flip_card)

# -------------- Wordlist
try:
    word_list = pandas.read_csv("data/french_words_to_learn.csv")
except FileNotFoundError:
    word_list = pandas.read_csv("data/french_words.csv")
    words_to_learn = word_list.to_dict(orient="records")
else:
    words_to_learn = word_list.to_dict(orient="records")

new_word = None





# ------------ UI --------------------------------------
window = Tk()
window.minsize(width=900, height=626)
window.config(bg=BACKGROUND_COLOR, padx = 50, pady= 50)
window.title("Flashy")

# TODO Card front
card_front_img = PhotoImage(file="/home/eden/PycharmProjects/flashy/images/card_front.png")
card_back_img = PhotoImage(file="/home/eden/PycharmProjects/flashy/images/card_back.png")
correct_img = current_card = PhotoImage(file="/home/eden/PycharmProjects/flashy/images/right.png")
incorrect_img = current_card = PhotoImage(file="/home/eden/PycharmProjects/flashy/images/wrong.png")


# TODO Q/A Prompts

current_card = Canvas(width=800, height=526, bg= BACKGROUND_COLOR)
current_card_side = current_card.create_image(400, 256, image=card_front_img)
current_card.grid(row=0, column = 0, columnspan= 2)

language_text_label = current_card.create_text(400, 150)
current_word = current_card.create_text(400, 263)

current_card.itemconfig(language_text_label, text = "French", font = LANGUAGE_FONT)
current_card.itemconfig(current_word, text = "", font = WORD_FONT)

# card_front.insert(language_text_label, 12, "new")




# TODO Correct/Incorrect Buttons
correct_button = Button(background = BACKGROUND_COLOR, highlightthickness = 0,image = correct_img, command=answer_correct)
correct_button.grid(row=1, column=1)

incorrect_button = Button(background = BACKGROUND_COLOR, highlightthickness = 0, image = incorrect_img, command=answer_incorrect)
incorrect_button.grid(row=1, column=0)


show_next_word()
window.mainloop()
