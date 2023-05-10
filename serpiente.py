from turtle import *
from random import randrange, choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colors = ['blue', 'green', 'orange', 'purple', 'yellow']

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    "Move food to a random position."
    while True:
        x = randrange(-19, 20) * 10
        y = randrange(-19, 20) * 10
        if vector(x, y) not in snake:
            food.x = x
            food.y = y
            break

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        move_food()
    else:
        snake.pop(0)

    clear()

    for i, body in enumerate(snake):
        square(body.x, body.y, 9, colors[i % len(colors)])  # Asignar colores aleatorios a la serpiente

    square(food.x, food.y, 9, choice(colors))  # Asignar un color aleatorio a la comida
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move_food()  # Move food to a random position initially
move()
done()
