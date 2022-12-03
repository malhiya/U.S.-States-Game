import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
# creating/adding a new shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        # List comprehension
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("to_learn.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item()) # or just use answer_state


turtle.mainloop() # keeps screen open replacess exitonclick

