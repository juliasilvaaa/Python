import turtle as t
import time

# Configuração da tela
tela = t.Screen()
tela.title("Super Cobra 9000 GTX FURY")
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.tracer(0)  # travamos as animações

# Cabeça da cobra
head = t.Turtle()
head.shape("square")
head.color('red')
head.penup()

# Lista para os segmentos
segmentos = []

# Maçã
maca = t.Turtle()
maca.shape('circle')
maca.color('red')
maca.penup()
maca.goto(100, 0)

# Funções de movimento
def mover_cima():
    if head.heading() != 270:
        head.setheading(90)

def mover_baixo():
    if head.heading() != 90:
        head.setheading(270)

def virar_direita():
    if head.heading() != 180:
        head.setheading(0)

def virar_esquerda():
    if head.heading() != 0:
        head.setheading(180)

# Criar novo segmento
def criar_seguimento():
    novo = t.Turtle()
    novo.shape("square")
    novo.color("yellow")
    novo.penup()
    segmentos.append(novo)

# Teclado
tela.listen()
tela.onkeypress(mover_cima, "w")
tela.onkeypress(mover_baixo, "s")
tela.onkeypress(virar_direita, "d")
tela.onkeypress(virar_esquerda, "a")

# Loop principal
while True:
    tela.update()
    time.sleep(0.1)

   
    for i in range(len(segmentos) - 1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x, y)

    
    if len(segmentos) > 0:
        segmentos[0].goto(head.xcor(), head.ycor())

    head.forward(20)

    # Colisão com a maçã
    if head.distance(maca) < 20:
        print("Nhom Nhom Nhom!")
        criar_seguimento()
        maca.goto(200, 100)

   
    # colisão com bordas da tela (limites de x e y)
    if head.xcor() >= 390:
        print('Ouch, bati na parede da direita!')
        head.setx(390)
    if head.xcor() <= -390:
        print('Ouch, bati na parede da esquerda!')
        head.setx(-390)
    if head.ycor() >= 290:
        print('Ouch, bati no teto!')
        head.sety(290)
    if head.ycor() <= -290:
        print('Ouch, bati no chão!')
        head.sety(-290)

# Fim
tela.mainloop()
