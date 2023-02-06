import turtle as t


class Turtle_Runner:
    def __init__(self, color, starting_pos):
        runner = t.Turtle()
        runner.shape("turtle")
        runner.color(color)
        runner.penup()
        runner.sety(starting_pos)


colors = ('red', 'green', 'blue', 'purple', 'yellow', 'orange')
position = 0
for x in range(6):
    runner1 = Turtle_Runner(colors[x], position)
    position += 40

screen = t.Screen()
screen.exitonclick()
