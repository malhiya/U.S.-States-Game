import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
# creating/adding a new shape
image = "Users/malihya/PycharmProjects/Udemy/U.S. States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("Users/malihya/PycharmProjects/Udemy/U.S. States Game/50_states.csv")
states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        # missing_states = []
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
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

# states to .csv



# #stack overflow
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop() # keeps screen open replacess exitonclick

