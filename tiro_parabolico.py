#Importar librerias
from random import randrange
from turtle import *
from freegames import vector

# Valores iniciales
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#Funcion para que responda al tocar en algun punto de la pantalla
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()
#Función para avanzar más rápido
def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 2  # Aumenta la velocidad de movimiento de los balones
        # RHace 
        if not inside(target):
            target.x = 200  

    if inside(ball):
        speed.y -= 0.2  # Aumenta la velocidad de movimiento del proyectil
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    ontimer(move, 25)  # Ajusta el tiempo de espera para un movimiento más rápido

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()