import turtle
import random
import math

# Crear la ventana de dibujo
screen = turtle.Screen()
screen.bgcolor("grey")  # Color de fondo de la ventana

# Crear una tortuga para dibujar el triángulo
t = turtle.Turtle()
t.speed(0)  # velocidad de dibujo máxima
t.hideturtle()  # Oculta la tortuga para hacer el dibujo más limpio

# Lado del triángulo
lado = 600  # tamaño del triángulo

# Calcular la altura del triángulo
altura = (math.sqrt(3) / 2) * lado

# Definir los vértices del triángulo equilátero
v1 = (-lado / 2, -altura / 2)  # Vértice 1
v2 = (lado / 2, -altura / 2)   # Vértice 2
v3 = (0, altura / 2)           # Vértice 3

# Dibujar un triángulo equilátero
def dibujar_triangulo():
    t.penup()
    t.goto(v1)
    t.pendown()
    t.goto(v2)
    t.goto(v3)
    t.goto(v1)

dibujar_triangulo()

# Crear una tortuga para los puntos
p = turtle.Turtle()
p.penup()
p.speed(0)  # Velocidad máxima para que se dibujen rápido
p.hideturtle()

# Función para encontrar el punto medio entre dos puntos
def punto_medio(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Colocar el primer punto aleatorio dentro del triángulo
punto_actual = (random.uniform(-lado / 2, lado / 2), random.uniform(-altura / 2, altura / 2))

# Colocar un punto en la posición actual
p.goto(punto_actual)
p.dot(3, "red")  # Dibujar el primer punto

# Iterar 100,000 veces para aplicar el algoritmo de Chaos Game
for _ in range(100000):
    # Elegir uno de los vértices al azar
    vertice = random.choice([v1, v2, v3])
    
    # Encontrar el punto medio entre el punto actual y el vértice seleccionado
    punto_actual = punto_medio(punto_actual, vertice)
    
    # Dibujar el nuevo punto
    p.goto(punto_actual)
    p.dot(2, "yellow")  # El tamaño del punto es de 2 píxeles y color blanco

# Finalizar el dibujo
turtle.done()

