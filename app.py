from flask import Flask, render_template
app = Flask(__name__)

# POSTS MOCK
posts = [
    {
        "titulo": "post1",
        "texto": "meu primeiro texto"
    },
    {
        "titulo": "post2",
        "texto": "meu segundo texto"
    }
    ,
    {
        "titulo": "post3",
        "texto": "meu terceiro texto"
    }
]

@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas1.html", entradas=posts)

@app.route('/teste')
def hello():
    return "Alguma coisa "