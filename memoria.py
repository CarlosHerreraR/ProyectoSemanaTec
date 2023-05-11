#Importar librerías
from random import *
from turtle import *
from freegames import path

#Declarar parámetros iniciales
car = path('car.gif')
tiles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ', 'O', 'P','Q','R','S','T','U','V','X','Y','Z','#','$','%','&','¿','?'] * 2
state = {'mark': None}
hide = [True] * 64
num_taps = 0  # Variable global para contar el número de taps
taps_display = Turtle()  # Objeto Turtle para mostrar el número de taps

#Función para trazar la cuadrícula del memorama
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

#Función para convertir coordenadas en índices de la cuadrícula
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

#Función para convertir títulos de la cuadrícula en coordenadas
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

num_taps = 0
#Función para contar los taps realizados en el tablero
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global num_taps  # Acceder a la variable global
    num_taps += 1
    taps_display.clear()  # Limpiar la pantalla antes de escribir el nuevo valor
    taps_display.write(f"Taps: {num_taps}", font=('Arial', 16, 'normal'))  # Escribir el nuevo valor
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

# Crear la pantalla y el marcador de taps
setup(420, 420, 370, 0)
taps_display = Turtle(visible=False)
taps_display.penup()
taps_display.goto(0, 190)

#Función mensaje todas las tarjetas abiertas
def all_open():
    "Check if all tiles are open."
    return all(not tile_hidden for tile_hidden in hide)

#Función para dibujar la imagen y las tarjetas
def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 17, y + 5)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    if all_open():
        taps_display.goto(0, 160)
        taps_display.write("¡Todos los cuadros están abiertos!", align='center', font=('Arial', 16, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()

taps_display.hideturtle()  # Ocultar el cursor de la Turtle que muestra el número de taps
done()
