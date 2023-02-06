# I admit, making a class of a class seems sloppy
# (class Turtle_Runner using a Turtle object already built
# into turtle lib). Just wnated to practice some additional
# class coding just to build the habit where feasible. THis probably
# wasnt a feasible moment :(


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
        distance = random.randint(0, 10)
        self.runner.forward(distance)


colors = ('Red', 'Green', 'Blue', 'Purple', 'Yellow', 'Orange')
screen = t.Screen()
# screen.setup(width=600,height=500)
your_bet = screen.textinput('Place your bet',
                            "Pick which turtle will win... choose either Red, Green, Blue, Purple, Yellow, Orange")

position = 0
contestants = []

for x in range(6):
    contestant = Turtle_Runner(colors[x], position)
    position += 40
    contestants.append(contestant)
for x in contestants:
    if x.runner.pencolor() == your_bet:
        x.pick = 1

y = 0
while contestants[y].runner.xcor() <= 250:
    for x in range(6):
        y = random.randint(0, 5)
        contestants[y].race()
        print(f"Color: {contestants[y].runner.color()}Position: {contestants[y].runner.pos()}\n{contestants[y].pick}")
        if contestants[y].runner.xcor() >= 250:
            print(f"{contestants[y].runner.pencolor()} Turtle is the winner")
            if contestants[y].pick == 1:
                print("You win!")
            else:
                print("You lose!")

screen.exitonclick()
