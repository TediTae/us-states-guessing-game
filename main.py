import turtle
import pandas

screen = turtle.Screen()
data = pandas.read_csv("50_states.csv")
screen.title("U.S. Guess States Game")
#This is a blank U.S. states image. Turtle only works with .gif so set it up like that.
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_list = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:

    guess_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess a State", prompt="Whats the State name?").title()
    #You can exit the game with typing exit.
    if guess_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guess_state:
                missing_states.append(state)
        #After you exited the game you can check your unguessed states from that .csv file and learn which states you couldnt get.
        learn_data = pandas.DataFrame(missing_states)
        learn_data.to_csv("states_to_learn")
        break
    if guess_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == guess_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(guess_state)
        guessed_state.append(guess_state)








