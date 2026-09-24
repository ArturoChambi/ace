import os
from flask import Flask, render_template, request, redirect, url_for, session, make_response, flash
from models import db, Usuario, Curso

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'clave_secreta_local')

# --- Configuración de la base de datos ---
# En local: SQLite. En Render: PostgreSQL (via variable DATABASE_URL)
database_url = os.environ.get('DATABASE_URL', 'sqlite:///cursos.db')

# Render da "postgres://" pero SQLAlchemy 2.x necesita "postgresql://"
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def index():
    usuario_preferido = request.cookies.get('usuario_preferido')
    return render_template('index.html', usuario_preferido=usuario_preferido)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        usuario = Usuario.query.filter_by(username=username).first()

        if usuario and usuario.password == password:
            session['usuario'] = usuario.username
            respuesta = redirect(url_for('lista_cursos'))
            respuesta.set_cookie('usuario_preferido', usuario.username, max_age=60*60*24*30)
            return respuesta
        else:
            error = "Usuario o contraseña incorrectos."

    return render_template('login.html', error=error)


@app.route('/cursos')
def lista_cursos():
    cursos = Curso.query.all()
    return render_template('cursos.html', cursos=cursos)


@app.route('/perfil')
def perfil():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('perfil.html', usuario=session['usuario'])


@app.route('/logout')
def logout():
    session.clear()
    flash("Sesion cerrada correctamente.")
    return redirect(url_for('index'))


@app.route('/eliminar_cookie')
def eliminar_cookie():
    respuesta = redirect(url_for('index'))
    respuesta.delete_cookie('usuario_preferido')
    return respuesta


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)