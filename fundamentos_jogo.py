import turtle
import time
tela = turtle.Screen()
tela.title("Eventos")
tela.bgcolor("white")
tela.setup(width=800, height=600)
tela.tracer(0)   #Trava as animações

def andar():
    jogador.forward(10)

def voltar():
    jogador.backward(10)

def virar_esquerda():
    jogador.setheading(jogador.heading()+5)

def virar_direita():
    jogador.setheading(jogador.heading()-5)
def crescer_tartaruga():
    jogador.shapesize(1.75, 1.75)
    jogador.write("Nhom Nhom Nhom", move=False)

# Instaciando o jogador
jogador = turtle.Turtle()
jogador.shape("turtle")
jogador.shapesize(1.5, 1.5)

# Criando obstaculo
alface = turtle.Turtle()
alface.color('black')
alface.shape('circle')
alface.penup()
alface.goto(300,250)


# Tela / Screen agora rastreia os cliques e telas precionadas
tela.listen()
tela.onkeypress(key='w', fun=andar)
tela.onkeypress(key='s', fun=voltar)
tela.onkeypress(key='a', fun=virar_esquerda)
tela.onkeypress(key='d', fun=virar_direita)

jogo_rodando = True
while jogo_rodando:
    time.sleep(0.016)
    tela.update() # Volta a animação
    if jogador.distance(alface) <= 30:
        print("nhom nhom nhom")
        alface.goto(1000,1000)
    if jogador.xcor() >=390:
        print("Ouch, bati na parede")
        jogador.backward(20)
    if jogador.xcor() <-390:
        print("Ouch, bati na parede")
        jogador.forward(20)
tela.mainloop()