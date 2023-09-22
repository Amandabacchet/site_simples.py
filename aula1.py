from flask import Flask, render_template

app = Flask(__name__)


# essa é a primerira pagina (homepage)
@app.route("/")
def homepage():
    # esse é um codigo para linkar o pyton no arquivo HTML
    return render_template("homepage.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuario.html", nome_usuario=nome_usuario)

    
# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

# servidor do heroku ainda para instalar 