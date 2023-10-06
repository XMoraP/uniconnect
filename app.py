from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
import os

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'uni-connect.mysql.database.azure.com'  # Cambia esto si tu servidor MySQL no está en localhost
app.config['MYSQL_USER'] = 'XMoraP'
app.config['MYSQL_PASSWORD'] = '12345678u$'
app.config['MYSQL_DB'] = 'uniconnect'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Ruta para mostrar datos de la base de datos
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

# Ruta para agregar un nuevo registro a la base de datos
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['name']
        apellido = request.form['last_name']
        email = request.form['email']
        contrasenna = request.form['password']

        # Realiza la inserción en la base de datos aquí
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (nombre, apellido, email, contrasenna) VALUES (%s, %s, %s, %s)",
                    (nombre, apellido, email, contrasenna))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/home')
def home():
    # Lógica de la vista de la página principal (home)
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtén los datos del formulario de inicio de sesión
        email = request.form['email']
        contrasenna = request.form['password']

        # Crea un cursor para interactuar con la base de datos
        cur = mysql.connection.cursor()

        # Obtiene la contraseña almacenada para el usuario
        cur.execute("SELECT contrasenna FROM user WHERE eMail = %s", [email])
        result = cur.fetchone()

    if result:
    # Comprueba si la contraseña ingresada coincide con la almacenada
        if contrasenna == result['contrasenna']:
        # Inicio de sesión exitoso, establece una sesión
            session['logged_in'] = True
            session['email'] = email

            return redirect(url_for('home'))
        else:
        # Contraseña incorrecta
            error = 'Contraseña incorrecta'
    else:
        # Usuario no encontrado
        error = 'Usuario no encontrado'

    cur.close()

    return render_template('home.html', error=error)
    
if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)