import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

NUMBER_OF_STATES = 50
correct_state_names = 0

states_data = pd.read_csv("50_states.csv")
state_name_list = states_data['state'].to_list()
guessed_states = []

# Insert State Name Text
insert_state_name = turtle.Turtle()
insert_state_name.penup()
insert_state_name.hideturtle()
insert_state_name.color('blue')
game_is_on = True

while game_is_on:
    if correct_state_names == NUMBER_OF_STATES:
        break
    user_answer = screen.textinput(title=f"{correct_state_names}/{NUMBER_OF_STATES} States Correct",
                                   prompt="Guess a State").capitalize()
    if user_answer == 'Exit':
        break
    elif user_answer in state_name_list:
        correct_state_names+=1
        guessed_states.append(user_answer)
        state_row = states_data[states_data['state'] == user_answer]
        insert_state_name.goto(int(state_row.x), int(state_row.y))
        insert_state_name.write(f"{user_answer}", align="center", font=("Arial", 12, "normal"))


missing_states = [state for state in state_name_list if (not state in guessed_states)]

df = pd.DataFrame(missing_states)
df.to_csv('state_names_to_learn.csv')

turtle.mainloop()