import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

answer_state = screen.textinput(title ="Guess the State", prompt = "What's another state's name?")

#if answer_sate is one of the states in all the states of the 50_states.csv
if answer_state in all_states:
    #if they got it right:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto()
        #Create a turtle to write the name of the state at the state's x and y coordate


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

# screen.exitonclick()