import random
import turtle as t


class Turtle_Runner:
    def __init__(self, color, starting_pos,speed):
        self.runner = t.Turtle()
        self.runner.shape("turtle")
        self.runner.color(color)
        self.runner.penup()
        self.runner.sety(starting_pos)
        self.runner.speed(speed)
        print(speed)

    def race(self):
        self.runner.forward(100)



colors = ('red', 'green', 'blue', 'purple', 'yellow', 'orange')
position = 0
contestants = []
speeds = [0,3,6,10,0]
for x in range(6):
    speed = random.choice(speeds)
    contestant = Turtle_Runner(colors[x], position,speed)
    position += 40
    contestants.append(contestant)
    print(speed)

for x in range(6):
    contestants[x].race()
screen = t.Screen()
screen.exitonclick()
