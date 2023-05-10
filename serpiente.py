from turtle import *
from random import randrange, choice
from freegames import square, vector

food = vector(0, 0)  # Posición inicial de la comida
snake = [vector(10, 0)]  # Posición inicial de la serpiente
aim = vector(0, -10)  # Dirección inicial de la serpiente

colors = ['blue', 'green', 'orange', 'purple', 'yellow']  # Colores disponibles para la serpiente y la comida

def change(x, y):
    """Cambiar la dirección de la serpiente."""
    aim.x = x
    aim.y = y

def inside(head):
    """Devuelve True si la cabeza está dentro de los límites."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """Mueve la comida a una posición aleatoria."""
    while True:
        x = randrange(-19, 20) * 10
        y = randrange(-19, 20) * 10
        if vector(x, y) not in snake:
            food.x = x
            food.y = y
            break

def move():
    """Mueve la serpiente hacia adelante un segmento."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # Dibuja la cabeza de la serpiente en rojo si está fuera de los límites o se superpone
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))  # Imprime la longitud de la serpiente cuando come la comida
        move_food()
    else:
        snake.pop(0)

    clear()

    for i, body in enumerate(snake):
        square(body.x, body.y, 9, colors[i % len(colors)])  # Asigna colores aleatorios a los segmentos de la serpiente

    square(food.x, food.y, 9, choice(colors))  # Asigna un color aleatorio a la comida
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
move_food()  # Mueve la comida a una posición aleatoria inicialmente
move()
done()