from flask import Flask, render_template, url_for


usuario = [{ 'nome': 'tiburcio',
            'seguidores': '12',
            'seguindo': '10'

}]

# Tipos
# jpg, png, gif, webp (pequeno permite tudo) , bmp, jfif


# --- Templates (modelos)
# -- Estrutura para criar html


# --- Static (estaticos/não-dinamicas/não muda)
# -- Tudo que está nela fica visivel

app = Flask(__name__)

# 
@app.route("/")
def firt_page():
    return render_template("index.html")

@app.route("/usuario")
def aboutuser_page():
    return render_template("usuario.html", usuario=usuarios[0])


# Rota de todos os usuarios, aqui vamos listar todos usuarios da plataforma
@app.route("/usuarios")
def listar_usuarios():
    return render_template("usuarios.html", usuario = usuarios)

@app.route("/enviar", methods=["POST"])
def salvar_leads():
    print(request.form)
    with open("leads.txt", mode="w", encoding="UTF-8") as file:
        nome_pessoa = request.form.get("nome")
        zap_pessoa = request.form.get("zap")
        email_pessoa = request.form.get("email")
        linha = f"{nome_pessoa} | {zap_pessoa} | {email_pessoa}"
        file.write(linha)
    return "Recebemos seus dados"


# Atualizar sozinho sem precisar rodar novamente a aplicação
app.run(debug=True)