#Importar librerías
from random import choice
from turtle import *
from freegames import floor, vector

# Marcador 
state = {'score': 0}
# Configuración de la ventana
path = Turtle(visible=False)
writer = Turtle(visible=False)
# Movimiento de packman
aim = vector(5, 0)
pacman = vector(-40, -80)
# Parametros de los fantasmas
ghosts = [
    [vector(-180, 160), vector(85, 0)],
    [vector(-180, -160), vector(0, 85)],
    [vector(100, 160), vector(0, -85)],
    [vector(100, -160), vector(-85, 0)],
    [vector(50, 160), vector(0, -85)],
    [vector(50, -160), vector(0, 85)],
    
]
#Mapa del juego 
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 
    0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,
    0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
    0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0,
    0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0,
    0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0,
    0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0,
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0,
    0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0,
    0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
    0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

]
# Definimos funciones
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()
# Puntos de desplazamiento 
def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

# Parametros visuales del mapa
def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')
# Movimiento de los personajes
def move():
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])  # Actualizar la puntuación mostrada en pantalla

    clear()  # Limpiar la pantalla

    if valid(pacman + aim):  # Comprobar si el movimiento de Pacman es válido
        pacman.move(aim)  # Mover a Pacman en la dirección deseada

    index = offset(pacman)  # Calcular el índice correspondiente a la posición de Pacman

    if tiles[index] == 1:  # Si Pacman come un punto
        tiles[index] = 2  # Marcar el punto como comido
        state['score'] += 1  # Incrementar la puntuación
        x = (index % 20) * 20 - 200  # Calcular la coordenada x para dibujar un cuadrado
        y = 180 - (index // 20) * 20  # Calcular la coordenada y para dibujar un cuadrado
        square(x, y)  # Dibujar un cuadrado en la posición del punto comido

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')  # Dibujar un círculo amarillo para representar a Pacman

    for point, course in ghosts:  # Iterar sobre cada fantasma
        if valid(point + course):  # Comprobar si el movimiento del fantasma es válido
            point.move(course)  # Mover al fantasma en la dirección deseada
        else:  # Si el movimiento no es válido
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)  # Elegir una nueva dirección de movimiento aleatoria para el fantasma
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')  # Dibujar un círculo rojo para representar al fantasma

    update()  # Actualizar la pantalla

    for point, course in ghosts:
        if abs(pacman - point) < 20:  # Comprobar si Pacman y el fantasma están lo suficientemente cerca
            return  # Terminar la función move si Pacman es atrapado por un fantasma

    ontimer(move, 100)  # Llamar a la función move nuevamente después de 100 milisegundos


def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()