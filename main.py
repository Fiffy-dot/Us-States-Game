import turtle
import pandas
import csv

# set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
states_image = "blank_states_img.gif"
screen.addshape(states_image)
turtle.shape(states_image)


# a function for writing the states on the map
def add_state(state, x, y):
    turtle_write = turtle.Turtle()
    turtle_write.hideturtle()
    turtle_write.color("black")
    turtle_write.penup()
    turtle_write.goto(x, y)
    turtle_write.write(state, align="center", font=("Courier", 8, "normal"))


# create a loop for the user to guess all the states
score = 0
correct_states = []
game_on = True
answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?").title()
while game_on:
    if score >= 50:
        game_on = False
    data = pandas.read_csv("50_states.csv")
    states_list = data["state"].to_list()
    # we check that the user hasn't already that state
    if answer_state not in correct_states:
        # we check if the guess is among the 50 states
        if answer_state in states_list:
            # add the correct guess onto the map
            # we get the position of the state
            pos = data[data.state == answer_state]
            x_cor = int(pos.x)
            y_cor = int(pos.y)
            add_state(answer_state, x_cor, y_cor)

            # add the correct guesses in a list
            correct_states.append(answer_state)

            # track the score
            score += 1
    # start displaying the score as the user plays
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another State's name?").title()

screen.exitonclick()
