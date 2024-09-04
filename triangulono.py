import turtle

def dibujarTriangulo(puntos,color,miTortuga):
    miTortuga.fillcolor(color)
    miTortuga.up()
    miTortuga.goto(puntos[0][0],puntos[0][1])
    miTortuga.down()
    miTortuga.begin_fill()
    miTortuga.goto(puntos[1][0],puntos[1][1])
    miTortuga.goto(puntos[2][0],puntos[2][1])
    miTortuga.goto(puntos[0][0],puntos[0][1])
    miTortuga.end_fill()

def obtenerMitad(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(puntos,grado,miTortuga):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    dibujarTriangulo(puntos,colormap[grado],miTortuga)
    if grado > 0:
        sierpinski([puntos[0],
                        obtenerMitad(puntos[0], puntos[1]),
                        obtenerMitad(puntos[0], puntos[2])],
                   grado-1, miTortuga)
        sierpinski([puntos[1],
                        obtenerMitad(puntos[0], puntos[1]),
                        obtenerMitad(puntos[1], puntos[2])],
                   grado-1, miTortuga)
        sierpinski([puntos[2],
                        obtenerMitad(puntos[2], puntos[1]),
                        obtenerMitad(puntos[0], puntos[2])],
                   grado-1, miTortuga)

def main():
   miTortuga = turtle.Turtle()
   miVentana = turtle.Screen()
   misPuntos = [[-100,-50],[0,100],[100,-50]]
   sierpinski(misPuntos,3,miTortuga)
   miVentana.exitonclick()

main()
