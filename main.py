import random
import turtle as t


class Turtle_Runner:
    def __init__(self, color, starting_pos):
        self.runner = t.Turtle()
        self.runner.shape("turtle")
        self.runner.color(color)
        self.runner.penup()
        self.runner.sety(starting_pos)
        self.runner.setx(-400)
        self.pick = 0

    def race(self):
        self.runner.forward(10)
        print(f"Color: {self.runner.color()}Position: {self.runner.pos()}")


colors = ('Red', 'Green', 'Blue', 'Purple', 'Yellow', 'Orange')
position = 0
contestants = []
for x in range(2):
    contestant = Turtle_Runner(colors[x], position)
    position += 40
    contestants.append(contestant)
your_bet = t.textinput('Place your bet', "Pick who will win... choose either Red, Green, Blue, Purple, Yellow, Orange")
for x in contestants:
    if x.runner.pencolor() == your_bet:
        x.pick = 1

y = 0
while contestants[y].runner.xcor() <= 210:
    for x in range(2):
        y = random.randint(0, 1)
        contestants[y].race()
        print(f"Color: {contestants[y].runner.color()}Position: {contestants[y].runner.pos()}\n{contestants[y].pick}")
        if contestants[y].runner.xcor() >= 210:
            print(f"Color: {contestants[y].runner.pencolor()} is the winner")
            if contestants[y].pick == 1:
                print("You win!")
            else:
                print("You lose!")

screen = t.Screen()
screen.exitonclick()
