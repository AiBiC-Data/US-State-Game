import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states =[]

while len(guessed_states) < 50:
    answer_state = screen.textinput(title =f"{len(guessed_states)}/50 States Correct", prompt = "What's another state's name?").title()
    if answer_state == 'Exit':
        missing_sates =[]
        for state in all_states:
            if state not in guessed_states:
                missing_sates.append(state)
        new_data = pandas.DataFrame(missing_sates)
        new_data.to_csv("states_to_learn.csv")
        break
    #if answer_sate is one of the states in all the states of the 50_states.csv
    if answer_state in all_states:
        guessed_states.append(answer_state)
        #if they got it right:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        #Create a turtle to write the name of the state at the state's x and y coordate
        t.write(answer_state)




# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

# screen.exitonclick()