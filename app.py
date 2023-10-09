#!/usr/bin/env python3.9
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
import os

app = Flask(__name__, template_folder="templates")

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'uni-connect.mysql.database.azure.com'  # Cambia esto si tu servidor MySQL no está en localhost
app.config['MYSQL_USER'] = 'XMoraP'
app.config['MYSQL_PASSWORD'] = '12345678u$'
app.config['MYSQL_DB'] = 'uniconnect'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_SSL_CA'] = './DigiCertGlobalRootCA.crt.pem'

mysql = MySQL(app)

# Ruta para mostrar datos de la base de datos
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    data = cur.fetchall()
    cur.close()
    return render_template('index2.html', data=data)



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
    return render_template('index2.html')


@app.route('/home')
def home():
    # Fetch user's profile information from your data source (e.g., session, database)
    user_profile = {
        'name': session.get('name'),
        'photo_url': 'static/images/userPhoto.png',  # Replace with the actual URL of the user's photo
        'role': 'Estudiante',  # Replace with the actual user's role
    }
    # Lógica de la vista de la página principal (home)
    return render_template('home.html', user_profile=user_profile)


@app.route('/login', methods=['GET', 'POST'])
def login():

    error = None

    if request.method == 'POST':
        # Obtén los datos del formulario de inicio de sesión
        email = request.form['email']
        contrasenna = request.form['password']

        # Crea un cursor para interactuar con la base de datos
        cur = mysql.connection.cursor()

        # Obtiene la contraseña almacenada para el usuario
        cur.execute("SELECT contrasenna, nombre, apellido FROM user WHERE eMail = %s", [email])
        result = cur.fetchone()

    if result:
    # Comprueba si la contraseña ingresada coincide con la almacenada
        if contrasenna == result['contrasenna']:
        # Inicio de sesión exitoso, establece una sesión
            session['logged_in'] = True
            session['email'] = email
            session['name'] = result['nombre']
            session['last_name'] = result['apellido']

            return redirect(url_for('dashboard'))
        else:
        # Contraseña incorrecta
            flash('Contraseña incorrecta', 'error')
    else:
        # Usuario no encontrado
        flash('Usuario no encontrado', 'error')

    return render_template('index2.html', error=error)

#DashBoard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

#Widgets
@app.route('/widgets')
def widgets():
    return render_template('widgets.html')

#Elements
@app.route('/general_elements')
def general_elements():
    return render_template('general_elements.html')

@app.route('/media_gallery')
def media_gallery():
    return render_template('media_gallery.html')

@app.route('/invoice')
def invoice():
    return render_template('invoice.html')

@app.route('/icons')
def icons():
    return render_template('icons.html')

#Tables
@app.route('/tables')
def tables():
    return render_template('tables.html')

#Apps
@app.route('/email')
def email():
    return render_template('email.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

#Pricing_Tables
@app.route('/price')
def price():
    return render_template('price.html')

#Contact
@app.route('/contact')
def contact():
    cur = mysql.connection.cursor()
    cur.execute("SELECT CONCAT(user.nombre, ' ', user.apellido) AS nombre_apellido, user.email, tutor.asignaturas_tutor FROM user INNER JOIN tutor ON user.id_user = tutor.id_tutor;")
    contacts = cur.fetchall()
    cur.close()
    return render_template('contact.html', contacts=contacts)

#Additional_Pages
@app.route('/profile')
def profile():
    # Fetch user's profile information from your data source (e.g., session, database)
    user_profile = {
        'name': session.get('name'),
        'photo_url': 'static/images/userPhoto.png',  # Replace with the actual URL of the user's photo
        'role': 'Estudiante',  # Replace with the actual user's role
    }

    return render_template('profile.html', user_profile=user_profile)


@app.route('/project')
def project():
    return render_template('project.html')

#Maps
@app.route('/map')
def map():
    return render_template('map.html')

#Charts
@app.route('/charts')
def charts():
    return render_template('charts.html')

#Settings
@app.route('/settings')
def settings():
    return render_template('settings.html')



if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)