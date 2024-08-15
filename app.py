from flask import Flask, render_template, request, redirect, url_for, session
from BaseDatos import BaseDatos
from Usuarios import Usuario, BaseUsuarios

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if request.method == 'POST':
            usermail = request.form['usermail']
            password = request.form['password']
            if (bu.authenticate(usermail, password) == True):
                user = bu.get_usuario(usermail)
                session['usermail'] = usermail
                session['id'] = user.id
                session['nombre'] = user.nombre
                session['logged_in'] = True
                return redirect('/') 
            else:
                msg = f'La contraseña es incorrecta para user con email: {usermail}'
                return render_template('login.hmtl', mensaje = msg)
            

@app.route('/por_titulo')
def titulos():
    lista_titulo = bd.get_titulos()
    return render_template('tabla.html',lista=lista_titulo,orden="titulo")

if __name__ == '__main__':
    bd = BaseDatos("peliculas.csv")
    bu = BaseUsuarios("usuarios.csv")
    app.run(debug=True)
