#!/usr/bin/env python3.9
<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, session, flash, Response, send_file
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
import os
import io 

=======
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
import os
import io
import base64
>>>>>>> de4bf908adb1aced5cdd1ac50f135c9d27605795

app = Flask(__name__, template_folder="templates")

app.config['UPLOAD_FOLDER'] = './files'
ALLOWED_EXTENSIONS= {'pdf', 'txt'}
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
    error = None
    if request.method == 'POST':
        nombre = request.form['name']
        apellido = request.form['last_name']
        email = request.form['email']
        contrasenna = request.form['password']

        if not nombre or not apellido or not email or not contrasenna:
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('registrarse'))

        cur0 = mysql.connection.cursor()
        cur0.execute("SELECT eMail from user WHERE eMail = %s", [email])
        result = cur0.fetchone()

        if result and result['eMail'] == email:

            flash('Este email ya esta en uso', 'error')
            return redirect(url_for('registrarse'))
            
        else:
            # Realiza la inserción en la base de datos aquí
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO user (nombre, apellido, email, contrasenna) VALUES (%s, %s, %s, %s)",
                        (nombre, apellido, email, contrasenna))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('index2'))     

    return render_template('index2.html', error=error)
 
@app.route('/login', methods=['GET', 'POST'])
def login():

    error = None
    result = None

    if request.method == 'POST':
        # Obtén los datos del formulario de inicio de sesión
        email = request.form['email']
        contrasenna = request.form['password']

        # Crea un cursor para interactuar con la base de datos
        cur = mysql.connection.cursor()

        # Obtiene la contraseña almacenada para el usuario
        cur.execute("SELECT contrasenna, nombre, apellido, status FROM user WHERE eMail = %s", [email])
        result = cur.fetchone()

        if not email or not contrasenna:
            #flash('Debe ingresar email y contraseña para iniciar sesion', 'error')
            return redirect(url_for('login'))    

    if result:
    # Comprueba si la contraseña ingresada coincide con la almacenada
        if contrasenna == result['contrasenna']:

        # Inicio de sesión exitoso, establece una sesión
            session['logged_in'] = True
            session['email'] = email
            session['name'] = result['nombre']
            session['last_name'] = result['apellido']
            session['status'] = result['status']

            return redirect(url_for('dashboard'))
        else:
        # Contraseña incorrecta
            flash('Email o contraseña incorrectos', 'error')

    return render_template('login.html', error=error)

#DashBoard
@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        user_profile = {
            'name': session['name'],
            'last_name': session['last_name']
        }
    else:
        user_profile = None


    return render_template('dashboard.html', user_profile=user_profile)
#Tables

@app.route('/tables')
def tables():
    if 'logged_in' in session:
        user_profile = {
            'name': session['name'],
            'last_name': session['last_name']
        }
    else:
        user_profile = None
    subject = None
    id_user= None
    session['id_user'] = id_user
    if request.method == 'POST':
         cur = mysql.connection.cursor()
         cur.execute("SELECT course_title FROM courses WHERE user_id = %s", [id_user])
         cur.fetchall()
         cur.close()

    return render_template('tables.html', user_profile=user_profile, subject = subject)

    
#Asignaturas
@app.route('/asignaturas')
def asignaturas():
    if 'logged_in' in session:
        user_profile = {
            'name': session['name'],
            'last_name': session['last_name']
        }
    else:
        user_profile = None

    return render_template('asignaturas.html', user_profile=user_profile)

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
    user_profile = None
    user_profile = {
        'name': session.get('name'),
        'last_name': session['last_name'],
        'email': session['email'],
        'status': session['status'],
        'photo_url': 'static/images/userPhoto.png',  # Replace with the actual URL of the user's photo
        'role': 'Estudiante',  # Replace with the actual user's role
    }
    mensaje = session.pop('mensaje', None)
    

    return render_template('profile.html', user_profile=user_profile, mensaje=mensaje)

# Perfil Tutor
@app.route('/profileTutor')
def profileTutor():
    # Fetch user's profile information from your data source (e.g., session, database)
    user_profile = {
        'name': session.get('name'),
        'last_name': session['last_name'],
        'photo_url': 'static/images/userPhoto.png',  # Replace with the actual URL of the user's photo
        'role': 'Estudiante',  # Replace with the actual user's role
    }

    return render_template('profileTutor.html', user_profile=user_profile)

# Dashboard Tutor
@app.route('/dashboardTutor')
def dashboardTutor():
    user_profile = None
    if 'logged_in' in session:
        user_profile = {
            'name': session['name'],
            'last_name': session['last_name'],
            'email': session['email'],
            'status': session['status']
        }
 
    return render_template('dashboardTutor.html', user_profile=user_profile)

# Guardar cambios del Perfil
@app.route('/guardar_perfil', methods=['POST'])
def guardar_perfil():
    
    user_profile = None
    mensaje = None
    error = None

    if request.method == 'POST':

        nombre = request.form['name']
        apellido = request.form['last_name']
        email = request.form['email']
        contrasenna = request.form['password']

        user_profile = {
            'name': session['name'],
            'last_name': session['last_name'],
            'status': session['status'],
            'email': session['email']
           
        }

        email_from_session = session["email"]
        cursor = mysql.connection.cursor()
        cursor2 = mysql.connection.cursor()

        # Obtener la contraseña almacenada asociada con el correo electrónico proporcionado
        cursor.execute("SELECT contrasenna, eMail FROM user WHERE eMail = %s", [email_from_session])
        cursor2.execute("SELECT eMail from user WHERE eMail <> %s", [email_from_session])
        resultado = cursor.fetchone()
        emails_existentes = cursor2.fetchone()

            # Comparar la contraseña proporcionada con la almacenada en la base de datos
        if contrasenna == resultado['contrasenna'] and not (emails_existentes['eMail'] == email):
                # Las contraseñas coinciden, actualizar el perfil
                cursor.execute("UPDATE user SET nombre = %s, apellido = %s, eMail = %s WHERE contrasenna = %s", [nombre, apellido, email, contrasenna])
                mysql.connection.commit()
                cursor.close()

                session['name'] = nombre
                session['last_name'] = apellido
                session['email'] = email

                session['mensaje'] = {'tipo': 'successUpdate', 'contenido': 'Perfil actualizado exitosamente'}
                return redirect(url_for('profile'))
        if emails_existentes['eMail'] == email:
                session['mensaje'] = {'tipo': 'errorEmail', 'contenido': 'Este correo electrónico ya esta en uso.'}
                return redirect(url_for('profile'))
        else:
             if not (contrasenna == resultado['contrasenna']):
                session['mensaje'] = {'tipo': 'errorPassword', 'contenido': 'La contraseña proporcionada es incorrecta. Por favor, inténtalo de nuevo.'}
                return redirect(url_for('profile'))

    return render_template('profile.html', user_profile=user_profile, mensaje=mensaje)

@app.route('/subir_imagen', methods=['POST'])
def subir_imagen():
    if 'imagen' in request.files:
        imagen = request.files['imagen']
        cursor = mysql.connection.cursor()
        
        if imagen:
            data =  imagen.read()
            cursor.execute("UPDATE user SET image = %s WHERE id_user = 34", (imagen.read(),))
            mysql.connection.commit()
            cursor.close()
    return "Imagen actualizada"

@app.route('/cargar_imagen')
def cargar_imagen():
    cur = mysql.connection.cursor()
    cur.execute("SELECT user.image FROM user WHERE user.id = 34;")
    image = cur.fetchone()
    cur.close()
    if image:
        return send_file(io.BytesIO(image[0], mimetype='image/png'))
    else:
        return "Imagen no encotrada", 404
    
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

#Boton Salir
@app.route('/salir', methods=['GET'])
def salir():
    session.clear()
    return render_template('index2.html')

@app.route('/registrarse',  methods=['GET', 'POST'])
def registrarse():
    return render_template('register.html')

@app.route('/index2',  methods=['GET', 'POST'])
def index2():
    return render_template('index2.html')

<<<<<<< HEAD
  
=======
<<<<<<< HEAD
@app.route('/cambiarContrasenna',  methods=['GET', 'POST'])
def cambiarContrasenna():
    
    if request.method == 'POST':
    
        email_from_session = session["email"]
        contrasenna = request.form['password']
        newPassword = request.form['newPassword']


        cur = mysql.connection.cursor()
        cur.execute("SELECT contrasenna FROM user WHERE eMail = %s", [email_from_session])
        result = cur.fetchone()

        if result['contrasenna'] == contrasenna: 
            
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE user SET contrasenna = %s WHERE contrasenna = %s", [newPassword, contrasenna])
            result = cur.fetchone()
            mysql.connection.commit()
            cursor.close()

            return redirect(url_for('profile'))
        
        else:
            flash('La contraseña proporcionada es incorrecta. Por favor, inténtalo de nuevo.', 'error')
            
    return render_template('/profile.html')

=======
@app.route('/upload', methods=['POST'])
def upload_file():
    # print("inicio")
    # for key, file in request.files.items():
    #     print("Campo: {key}")
    #     print("Nombre del archivo: {file.filename}")
    #     print("Tipo MIME: {file.mimetype}")
    #     print("Tamaño del archivo: {file.content_length} bytes")
    # print("fin")
    # return
    #if 'file' not in request.files:
     #   return 'No se seleccionó ningún archivo.'
>>>>>>> de4bf908adb1aced5cdd1ac50f135c9d27605795

    #subject = request.form['subject']
    #file = request.files['file']
    #id = 12

    #if file.filename == '':
        #return 'No se seleccionó ningún archivo.'

    #if file:
        # codificamos el archivo obtenido en formato binario para poder guardarlo posteriormente en la base de datos
        binario=base64.b64encode(file.read())
        
        # Subimos los datos biniarios a la base de datos de azure
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO courses(course_title, user_id, course_description, course_image) VALUES (%s, %s, %s, %s)",
         (subject, id, binario, file.filename))
        mysql.connection.commit()
        cur.close()

             #return redirect(url_for('tables'))
        decodificado=base64.b64decode(binari)
        return send_file(
             io.BytesIO(decodificado),
             mimetype='application/octet-stream',
             as_attachment=True,
             download_name=file.filename
         )
>>>>>>> 52d329bc4de409636d642d839d79907608ecb3bd



       




if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)

