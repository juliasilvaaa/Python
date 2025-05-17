# TkInter
# Turtle (mais ludico)
# Flet
# HTML, CSS <= Python Web

# Import turtle as apelido_desejado
import turtle as colors

tela = colors.Screen()
tela.title("Exibindo Cores")
tela.bgcolor("pink")
tela.setup(width=800, height=600)


rosa = colors.Turtle()
rosa.shape("turtle") # Arrow, tutle, circle, square, triangle
rosa.shapesize(2,2)
rosa.color("white")
rosa.pencolor("red")
rosa.pensize(4)


for lado in range(5):
    rosa.forward(100)
    # Dividir os angulos 360 pelos lados
    # / - Deixa em numero decimal - // Deixa em numero inteiro
    rosa.left(360 // 5)

# Quadrado
rosa.forward(100)
rosa.left(90)
rosa.forward(100)
rosa.left(90)
rosa.forward(100)
rosa.left(90)
rosa.forward(100)

# Triangulo - traço branco 
rosa.pencolor("white")
for lado in range(3):
    rosa.forward(100)
    rosa.left(360 // 3)


# Criando uma nova

azul = colors.Turtle()
azul.shape('turtle')
azul.color('blue')
azul.penup()
azul.goto(-300,285)


todas_cores = []
coordenadas_y = [245, 225, 185, 145, 105, 65, 25]
colors_pinture = ["red", "magenta", "cyan", "green", "orange", "gray", "black"]
for indice in range(7):
    print(indice)
    todas_cores.append(colors.Turtle())
    todas_cores[indice].shape("turtle")
    todas_cores[indice].shapesize(1.5,1.5)
    todas_cores[indice].color(colors_pinture[indice])
    todas_cores[indice].penup()
    todas_cores[indice].goto(-380, coordenadas_y[indice])

print(todas_cores)

import random
corrida_on = True
while corrida_on:
    for corredor in todas_cores:
       corredor.forward(random.randint(1,10))
       if corredor.xcor() >= 385:
           corrida_on = False
           print(f"A tartaruga {corredor.color()} venceu a corrida")
           corredor.goto(0,0)
           corredor.write("Ganhei",move=False, align='center', font=("Calibri", 16, "bold"))
           break





# Espera para fechar a tela quando clicar
tela.exitonclick()