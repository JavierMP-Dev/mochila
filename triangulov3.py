import turtle
import math

# Crear la ventana de dibujo
screen = turtle.Screen()
screen.bgcolor("grey")  # Color de fondo de la ventana que se crea

# Crear una tortuga, el cursor
t = turtle.Turtle()
t.speed(3)  #  velocidad de dibujo

# Lado del triángulo
lado = 600  # tamaño del triangulo

# Calcular la altura del triángulo
altura = (math.sqrt(3) / 2) * lado

# Mover la tortuga a la posición inicial
t.penup()  # Levanta el lápiz para no dibujar mientras se mueve
t.goto(-lado / 2, -altura / 2)  # Mover a la posición inicial calculada
t.pendown()  # Baja el lápiz para empezar a dibujar

# Dibujar un triángulo equilátero
for _ in range(3):
    t.forward(lado)  # Dibuja un lado del triángulo
    t.left(120)      # Gira la tortuga 120 grados a la izquierda

# Finalizar el dibujo
turtle.done()

