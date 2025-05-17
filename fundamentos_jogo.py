import turtle
tela = turtle.Screen()
tela.title("Eventos")
tela.bgcolor("white")
tela.setup(width=800, height=600)

def andar():
    jogador.forward(10)

def voltar():
    jogador.backward(10)

def virar_esquerda():
    jogador.setheading(jogador.heading()+5)

def virar_direita():
    jogador.setheading(jogador.heading()-5)

# Instaciando o jogador
jogador = turtle.Turtle()
jogador.shape("turtle")
jogador.shapesize(1.5, 1.5)

# Tela / Screen agora rastreia os cliques e telas precionadas
tela.listen()
tela.onkeypress(key='w', fun=andar)
tela.onkeypress(key='s', fun=voltar)
tela.onkeypress(key='a', fun=virar_esquerda)
tela.onkeypress(key='d', fun=virar_direita)

tela.mainloop()