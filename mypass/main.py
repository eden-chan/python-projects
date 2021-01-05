from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    generated_password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = email_username_entry.get()
    password = password_entry.get()

    new_data = {
       website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.askretrycancel(title=website, message=f"You left a field empty\n")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", mode = "w") as data_file:
                data.update(new_data)
                # updates
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            # pyperclip.copy(password)

# ---------------------------- Search for Password ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        print("There are no entries to search for.")
    else:
        try:
            username = data[website]["username"]
            password = data[website]["password"]
        except KeyError:
            messagebox.showerror(title=f"{website} not saved", message=f"You do not have any saved passwords for {website}")
        else:
            messagebox.showinfo(title=website, message= f"Your Username is {username}\n Your password is {password}\n")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.config(padx=20, pady=20, background="white")

# Logo
canvas = Canvas(width=200, height=200, bg="white")
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)
# Labels
website_label = Label(text="Website:", background="white")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:", background="white")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:", background="white")
password_label.grid(row=3, column=0)

search_button = Button(text="Search", width = 16, command = search_password)
search_button.grid(row=1, column = 2)
# Entries
website_entry = Entry(width=20)
website_entry.grid(row=1, column=1, columnspan=1)

email_username_entry = Entry(width=40)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "eden.chan102034@gmail.com")

password_entry = Entry(width=20)
password_entry.grid(row=3, column=1, columnspan=1)

# Buttons
generate_password_button = Button(text="Generate Password", width=16, command=generate_password)
generate_password_button.grid(row=3, column=2, columnspan=1)
add_password_button = Button(text="Add", width=20, command=save_password)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
