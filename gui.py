import tkinter
from tkinter import *
from tkinter import messagebox
import random
import string


FONT_NORMAL = ('Arial', 16,'normal')
FONT_FORTE = ('Arial', 18,'bold')

#1º Widget
#Widgets(ELEMENTOS, botão, inputs, rótulos, radio)
#2º Layout
#Layout(pack, grid, place)

tela = tkinter.Tk()
tela.title("Meu primeiro GUI - Graphical User Interface")
# tela.geometry("500x500")
tela.config(bg="white")

def teste():
    print("O botão foi apertado vigorosamente!")



def validar_entrada():
    info_site = entry_site.get()
    info_mail = entry_mail.get()
    info_senha = entry_senha.get()
    if not info_site or not info_mail or not info_senha:
        messagebox.showwarning(title="Ops", message="Preencha todos os campos")
        return False
    salvar_info(info_site,info_mail,info_senha)

# Função para salvar site, email e senha
def salvar_info(site, email, senha):
    import json
    linha = f"{site} | {email} | {senha}\n"
    senha_dicionario = {site: {'email': email, 'senha': senha}}
    print(senha_dicionario)

    with open(file="senhas.txt", mode="w", encoding="UTF-8") as file:
        json.dump(senha_dicionario, file, indent=4)
    messagebox.showinfo(message="Senha salva, Parabéns!👍")




def gerar_senha():
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = ''.join(random.choices(caracteres, k=12))
    entry_senha.delete(0, END)
    entry_senha.insert(0, senha)


#Widgets
splash = tkinter.PhotoImage(file="image_250.png")

canvas = tkinter.Canvas(width=250, height=250, background="white")
canvas.create_image(125,125, image=splash)

lbl_site = tkinter.Label(text="Site", foreground="black", bg="white", font=FONT_NORMAL, anchor="e", width=5)
lbl_mail = tkinter.Label(text="Email", foreground="black", bg="white", font=FONT_NORMAL, anchor="e", width=5)
lbl_senha = tkinter.Label(text="Senha", foreground="black", bg="white", font=FONT_NORMAL, anchor="e", width=5)

btn_pesquisar = tkinter.Button(text="Pesquisar")
btn_gerar = tkinter.Button(text="Gerar Senha", command=gerar_senha)
btn_salvar = tkinter.Button(text="Salvar Senha", command=validar_entrada)

entry_site = tkinter.Entry()
entry_mail = tkinter.Entry()
entry_senha = tkinter.Entry()

# Layout
canvas.grid(row=0, column=1)
lbl_site.grid(row=1, column=0, padx=8)
lbl_mail.grid(row=2, column=0, padx=8)
lbl_senha.grid(row=3, column=0, padx=8)

entry_site.grid(row=1, column=1, sticky="ew", padx=(0,8))
entry_mail.grid(row=2, column=1, columnspan=2, sticky="ew") #esticar para duas colunas
entry_senha.grid(row=3, column=1, sticky="ew", padx=(0,8))

btn_pesquisar.grid(column=2, row=1, sticky="ew")
btn_gerar.grid(column=2, row=3, sticky="ew")
btn_salvar.grid(column=1, row=4 , columnspan=2, sticky="ew")

tela.mainloop()