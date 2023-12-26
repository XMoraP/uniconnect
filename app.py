from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file, jsonify
from flask_mysqldb import MySQL, MySQLdb
from datetime import datetime
import io
import base64
import json
import binascii
from Contact import loginfo, crearDirectorio
import openai
from dotenv import load_dotenv
import os
import shutil

load_dotenv()



openai.api_key = os.getenv("API_KEY_IA") 

app = Flask(__name__, template_folder="templates")
app.debug = True
app.secret_key = os.getenv("APP_SECRET_KEY")

app.config['UPLOAD_FOLDER'] = './files'
ALLOWED_EXTENSIONS= {'pdf', 'txt'}

# Configuración de la base de datos
app.config['MYSQL_HOST'] = os.getenv("DB_HOST")  
app.config['MYSQL_USER'] = os.getenv("DB_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("DB_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("DB")
app.config['MYSQL_CURSORCLASS'] = os.getenv("CURSOSRCLASS")

mysql = MySQL(app)

# Ruta para mostrar datos de la base de  datos
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
    mensaje = None
    
    if request.method == 'POST':
        nombre = request.form['name']
        apellido = request.form['last_name']
        email = request.form['email']
        contrasenna = request.form['password']

        cur0 = mysql.connection.cursor()
        cur0.execute("SELECT eMail from user WHERE eMail = %s", [email])
        result = cur0.fetchone()

        if result and result['eMail'] == email:

            flash('El email ya está en uso', 'error')
            return redirect(url_for('registrarse'))
            
        else:
            # Realiza la inserción en la base de datos aquí
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO user (nombre, apellido, email, contrasenna) VALUES (%s, %s, %s, %s)",
                        (nombre, apellido, email, contrasenna))
            mysql.connection.commit()
            cur.close()

            session['mensaje'] = {'tipo': 'successUpdate', 'contenido': '¡Registro exitoso!'}
            return redirect(url_for('registrarse'))     

    return render_template('index2.html', error=error, mensaje=mensaje)
 
 
@app.route('/login', methods=['GET', 'POST'])
def login():

    error = None
    result = None

    if request.method == 'POST':
        email = request.form['email']
        contrasenna = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT id_user, contrasenna, nombre, apellido, status, nombre_grado FROM user WHERE eMail = %s", [email])
        result = cur.fetchone()

        if not email or not contrasenna:
            return redirect(url_for('login'))    

    if result:
        if contrasenna == result['contrasenna']:

            session['logged_in'] = True
            session['email'] = email
            session['id_user'] = result['id_user']
            session['name'] = result['nombre']
            session['last_name'] = result['apellido']
            session['status'] = result['status']
            session['nombre_grado'] = result['nombre_grado']

            return redirect(url_for('dashboard'))
            
        else:
            flash('Email o contraseña incorrectos', 'error')

    return render_template('login.html', error=error)

# Funcion auxiliar para obtener el perfil del usuario
def get_user_profile():
    return {
        'name': session.get('name'),
        'last_name': session['last_name'],
        'email': session['email'],
        'status': session['status'],
        'nombre_grado': session['nombre_grado'],
        'photo_url': 'static/images/userPhoto.png',
    }

#DashBoard
@app.route('/dashboard')
def dashboard():

    id_user = session['id_user']
    
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM events WHERE id_user = %s ORDER BY id", (id_user,))
    calendar = cur.fetchall()  

    user_profile = loginfo(session)

    return render_template('dashboard.html', user_profile=user_profile, calendar=calendar, longitud = num_notificaciones(), notificaciones = obtener_notificaciones(), tutor = isTutor())

#Archivos
@app.route('/archivos')
def archivos():
    user_profile = loginfo(session)
    return render_template('archivos.html', user_profile=user_profile, longitud = num_notificaciones(), notificaciones = obtener_notificaciones(),  tutor = isTutor())

#ArchivosTutor
@app.route('/archivosTutor')
def archivosTutor():
    user_profile = loginfo(session)

    return render_template('archivosTutor.html', user_profile=user_profile, longitud = num_notificaciones(), notificaciones = obtener_notificaciones(), tutor = isTutor())
 
#Asignaturas
@app.route('/asignaturas')
def asignaturas():
    user_profile = loginfo(session)
    return render_template('asignaturas.html', user_profile=user_profile)

#Contact
@app.route('/contact')
def contact():
    ruta = "static/Fotos_Tutor"
    cont = 0

    try:
        shutil.rmtree(ruta)
        print(f"Directorio {ruta} borrado exitosamente.")
    except OSError as e:
        print(f"Error al borrar el directorio {ruta}: {e}")

    user_profile = loginfo(session)
    crearDirectorio(ruta)
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM vista_ventana_tutores")
    contacts = cur.fetchall()
    cur.close()

    contacts_list = []
    isUser = session['name'] + "" + session['last_name']
    for result in contacts:
        id_user = result['id_user']
        nombre_apellido = result['nombre_apellido']
        email = result['email']
        asignaturas_tutor = result['asignaturas_tutor']
        image_data_hex = result['image']


        if image_data_hex:
            try:
                image_data = base64.b64decode(image_data_hex)

                with open(f'static/Fotos_Tutor/temp_image{cont}.jpg', 'wb') as f:
                    f.write(image_data)

                image_base64 = f"static/Fotos_Tutor/temp_image{cont}.jpg";

                cont = cont + 1

            except binascii.Error:
                image_base64 = "data:image/jpeg;base64," + base64.b64encode(open('static/images/userPhoto.png', 'rb').read()).decode('utf-8')
        else:
            image_base64 = "data:image/jpeg;base64," + base64.b64encode(open('static/images/userPhoto.png', 'rb').read()).decode('utf-8')

        contact = {
            'id_tutor': id_user,
            'nombre_apellido': nombre_apellido,
            'email': email,
            'asignaturas_tutor': asignaturas_tutor,
            'imagen': image_base64
        }

        if contact['nombre_apellido'] != isUser:
            contacts_list.append(contact)

    return render_template('contact.html', contacts=contacts_list, user_profile=user_profile, longitud = num_notificaciones(), notificaciones = obtener_notificaciones(), tutor = isTutor())


@app.route('/pedir_tutoria', methods=['POST'])
def pedir_tutoria():
    # Obtener el ID del tutor desde el formulario
    id_tutor = request.form.get('tutor_id')
    if id_tutor != session['id_user']:
        msg = f"El alumno {session['name']}-{session['last_name']} solicita una Tutoria"
        cur = mysql.connection.cursor()
        cur.execute("INSERT IGNORE INTO Tutoria(id_user, id_tutor, mensaje) VALUES(%s, %s, %s)", (session['id_user'], id_tutor, msg))
        mysql.connection.commit()
        cur.close()
    return redirect(url_for('contact'))

@app.route('/hacer_tutorando/aceptar', methods=['POST'])
def aceptar_tutorando():
    id_user = request.form.get('id_user')
    if id_user:
        msg = "Tutoria aceptada!!!"
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tutorando(id_tutor, id_user) VALUES(%s, %s)", (session['id_user'], id_user))
        mysql.connection.commit()
        cur.execute("INSERT INTO tutoria(id_user, id_tutor, mensaje) VALUES(%s, %s, %s)", (session['id_user'], id_user, msg))
        mysql.connection.commit()
        cur.execute("DELETE FROM tutoria WHERE id_user = %s AND id_tutor = %s", (id_user, session['id_user']))
        mysql.connection.commit()
        cur.close()
    return redirect(url_for('tutelados'))

@app.route('/hacer_tutorando/denegar', methods=['POST'])
def denegar_tutorando():
    id_user = request.form.get('id_user')
    if id_user:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM tutoria WHERE id_user = %s AND id_tutor = %s", (id_user, session['id_user']))
        mysql.connection.commit()
        cur.close()
    return redirect(url_for('contact'))

@app.route('/borras_Notis/<int:id_user>', methods=['POST'])
def borras_Notis(id_user):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tutoria WHERE id_user = %s AND id_tutor = %s", (id_user, session['id_user']))
    mysql.connection.commit()
    cur.close()

    # Envia una respuesta JSON con la URL de redirección
    return jsonify({'redirect': request.referrer})

#Tutelados
@app.route('/tutelados')
def tutelados():
    id = session['id_user']
    cur = mysql.connection.cursor()
    cur.execute("SELECT concat(user.nombre, user.apellido) AS nombre_completo, user.eMail AS email, user.nombre_grado AS grado FROM user, tutorando WHERE user.id_user = tutorando.id_user AND tutorando.id_tutor = %s", (id,))
    tutelados = cur.fetchall()
    user_profile = loginfo(session)
    return render_template('tutelados.html', user_profile=user_profile, tutelados = tutelados, longitud = num_notificaciones(), notificaciones = obtener_notificaciones(), tutor = isTutor())

@app.route('/profile')
def profile():
    user_profile = None
    user_profile = {
        'name': session.get('name'),
        'last_name': session['last_name'],
        'email': session['email'],
        'status': session['status'],
        'nombre_grado': session['nombre_grado'],
        'photo_url': 'static/images/userPhoto.png',
        'role': 'Estudiante',
    }
    mensaje = session.pop('mensaje', None)
    

    return render_template('profile.html', user_profile=user_profile, mensaje=mensaje, longitud = num_notificaciones(), notificaciones = obtener_notificaciones(), tutor = isTutor())

# Perfil Tutor
@app.route('/profileTutor', methods=['GET'] )
def profileTutor():    
    user_profile = None
    user_profile = {
        'name': session.get('name'),
        'last_name': session['last_name'],
        'email': session['email'],
        'status': session['status'],
        'nombre_grado': session['nombre_grado'],
        'photo_url': 'static/images/userPhoto.png',
        'role': 'Estudiante',
    }
    mensaje = session.pop('mensaje', None)

    return render_template('profileTutor.html', user_profile=user_profile, mensaje=mensaje, longitud = num_notificaciones(), notificaciones = obtener_notificaciones(), tutor = isTutor())

# Guardar cambios del Perfil
def is_email_in_use(email, email_from_session):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT eMail FROM user WHERE eMail <> %s", [email_from_session])
    return cursor.fetchone() and cursor.fetchone()['eMail'] == email

def is_password_correct(email, contrasenna):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT contrasenna FROM user WHERE eMail = %s", [email])
    resultado = cursor.fetchone()
    return resultado and contrasenna == resultado['contrasenna']

def update_user_profile(email, nombre, apellido, email_new, grado):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE user SET nombre = %s, apellido = %s, eMail = %s, nombre_grado = %s WHERE eMail = %s",
                   [nombre, apellido, email_new, grado, email])
    mysql.connection.commit()

@app.route('/guardar_perfil', methods=['POST'])
def guardar_perfil():
    user_profile = get_user_profile()
    mensaje = None

    if request.method == 'POST':
        email_from_session = session["email"]
        nombre = request.form['name']
        apellido = request.form['last_name']
        email_new = request.form['email']
        contrasenna = request.form['password']
        grado = request.form['grado']

        if is_email_in_use(email_new, email_from_session):
            session['mensaje'] = {'tipo': 'errorEmail', 'contenido': 'Este correo electrónico ya está en uso.'}
        elif not is_password_correct(email_from_session, contrasenna):
            session['mensaje'] = {'tipo': 'errorPassword', 'contenido': 'La contraseña proporcionada es incorrecta. Por favor, inténtalo de nuevo.'}
        else:
            update_user_profile(email_from_session, nombre, apellido, email_new, grado)

            session['name'] = nombre
            session['last_name'] = apellido
            session['email'] = email_new
            session['nombre_grado'] = grado
            session['mensaje'] = {'tipo': 'successUpdate', 'contenido': 'Perfil actualizado exitosamente'}

    return render_template('profile.html', user_profile=user_profile, mensaje=session.get('mensaje', None),
                           longitud=num_notificaciones(), notificaciones=obtener_notificaciones(), tutor=isTutor())

# Codigos para subir imagenes de perfil.
@app.route('/subir_imagen', methods=['POST'])
def subir_imagen():
    id_user = session['id_user']

    if 'imagen' in request.files:
        imagen = request.files['imagen']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT image from image WHERE id_user = %s", (id_user,))
        result = cursor.fetchall()
        mysql.connection.commit()

        if result:
            data = base64.b64encode(imagen.read())
            cursor.execute("UPDATE image SET image = %s WHERE id_user = %s", (data, id_user,))
            mysql.connection.commit()
            cursor.close()
            session['mensaje'] = {'tipo':'successUpdate','contenido':'imagen actualizada'}
            return redirect(url_for('profile'))
        else:
            data = base64.b64encode(imagen.read())
            cursor.execute("INSERT INTO image (id_user, image) VALUES (%s,%s)", (id_user, data,))
            mysql.connection.commit()
            cursor.close()
            session['mensaje'] = {'tipo':'successUpdate','contenido':'imagen actualizada Nuevo'}
            return redirect(url_for('profile'))

@app.route('/cargar_imagen')
def cargar_imagen():
    id_user = session['id_user']
    cur = mysql.connection.cursor()
    cur.execute("SELECT image FROM image WHERE id_user = %s", (id_user,))
    image_data = cur.fetchone()
    cur.close()
    if image_data is not None:
        # Decodifica la imagen en formato base64 para mostrarla
        image_bytes = base64.b64decode(image_data['image'])
        return send_file(io.BytesIO(image_bytes), mimetype='image/*')
    else:
        return send_file('static/images/userPhoto.png', mimetype='image/*')

#Boton Salir
@app.route('/salir', methods=['GET'])
def salir():
    session.clear()
    return render_template('index2.html')

@app.route('/registrarse',  methods=['GET', 'POST'])
def registrarse():
    mensaje = session.pop('mensaje', None)
    return render_template('register.html', mensaje=mensaje)

@app.route('/index2',  methods=['GET', 'POST'])
def index2():
    return render_template('index2.html')

# Cambiar contraseña de usuario
@app.route('/cambiarContrasenna',  methods=['GET', 'POST'])
def cambiarContrasenna():
    user_profile = None
    mensaje = None
    
    if request.method == 'POST':
    
        email_from_session = session["email"]
        contrasenna = request.form['password']
        newPassword = request.form['newPassword']
        confirmPassword = request.form['confirmPassword']


        cur = mysql.connection.cursor()
        cur.execute("SELECT contrasenna FROM user WHERE eMail = %s", [email_from_session])
        result = cur.fetchone()

        if result['contrasenna'] == contrasenna: 
            if newPassword == confirmPassword:
                cursor = mysql.connection.cursor()
                cursor.execute("UPDATE user SET contrasenna = %s WHERE contrasenna = %s", [newPassword, contrasenna])
                result = cur.fetchone()
                mysql.connection.commit()
                cursor.close()

                session['contrasenna']: newPassword
                session['mensaje'] = {'tipo':'successUpdate','contenido':'Contraseña actualizada'}
                if(session['status'] == 'Tutor'):
                    return redirect(url_for('profileTutor'))
                else:
                    return redirect(url_for('profile'))
            else:
                session['mensaje'] = {'tipo': 'errorPassword', 'contenido': 'Los campos Nueva contraseña y Confirmar contraseña no coinciden. Por favor, inténtalo de nuevo.'}
                if(session['status'] == 'Tutor'):
                    return redirect(url_for('profileTutor'))
                else:
                    return redirect(url_for('profile'))
        else:
            session['mensaje'] = {'tipo': 'errorPassword', 'contenido': 'La contraseña proporcionada es incorrecta. Por favor, inténtalo de nuevo.'}
            if(session['status'] == 'Tutor'):
                    return redirect(url_for('profileTutor'))
            else:
                    return redirect(url_for('profile'))
        
    return render_template('profile.html', user_profile=user_profile, mensaje=mensaje , longitud = num_notificaciones(), notificaciones = obtener_notificaciones(), tutor = isTutor())


# Funcion auxiliar para saber si el usuario es tutor o estudiante, y cambiar su rol
def update_user_status(email_from_session, contrasenna, new_status):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT contrasenna FROM user WHERE eMail = %s", [email_from_session])
    result = cursor.fetchone()

    if result and result['contrasenna'] == contrasenna:
        id_user = session["id_user"]
        cursor.execute("UPDATE user SET status = %s WHERE contrasenna = %s", [new_status, contrasenna])

        if new_status == 'Tutor':
            cursor.execute("INSERT INTO tutor (id_tutor) VALUES(%s)", [id_user])
        else:
            cursor.execute("DELETE FROM tutor WHERE id_tutor=%s", [id_user])

        mysql.connection.commit()

        cursor2 = mysql.connection.cursor()
        cursor2.execute("SELECT status FROM user WHERE eMail = %s", [email_from_session])
        resultado = cursor2.fetchone()
        mysql.connection.commit()

        session['status'] = resultado['status']
        return True

    return False

@app.route('/altaTutor', methods=['POST'])
def alta_tutor():
    email_from_session = session["email"]
    contrasenna = request.form['password']

    if update_user_status(email_from_session, contrasenna, 'Tutor'):
        session['mensaje1'] = {'tipo': 'successUpdate', 'contenido': 'Te has dado de alta como Tutor'}
    else:
        session['mensaje1'] = {'tipo': 'errorPassword', 'contenido': 'La contraseña proporcionada es incorrecta. Por favor, inténtalo de nuevo.'}

    return redirect(url_for('profileTutor'))

@app.route('/bajaTutor', methods=['POST'])
def baja_tutor():
    email_from_session = session["email"]
    contrasenna = request.form['password']

    if update_user_status(email_from_session, contrasenna, 'Estudiante'):
        session['mensaje1'] = {'tipo': 'successUpdate', 'contenido': 'Te has dado de baja de Tutor'}
    else:
        session['mensaje1'] = {'tipo': 'errorPassword', 'contenido': 'La contraseña proporcionada es incorrecta. Por favor, inténtalo de nuevo.'}

    return redirect(url_for('profile'))


# Cambiar las asignaturas del tutor
def is_password_correct_for_user(email_from_session, contrasenna):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT contrasenna FROM user WHERE eMail = %s", [email_from_session])
    result = cursor.fetchone()
    return result and result['contrasenna'] == contrasenna

def get_tutor_data(id_user):
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tutor WHERE id_tutor = %s", [id_user])
    return cursor.fetchone()

def update_tutor_data(id_user, asignaturas):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE tutor SET asignaturas_tutor = %s WHERE id_tutor = %s", [asignaturas, id_user])
    mysql.connection.commit()
    cursor.close()

def insert_tutor_data(id_user, asignaturas):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO tutor (id_tutor, asignaturas_tutor) VALUES (%s, %s)", [id_user, asignaturas])
    mysql.connection.commit()
    cursor.close()

@app.route('/camposTutor', methods=['POST'])
def campos_tutor():
    user_profile = None
    mensaje = None

    email_from_session = session["email"]
    contrasenna = request.form['password']
    asignaturas = request.form['asignaturas']
    id_user = session["id_user"]

    if is_password_correct_for_user(email_from_session, contrasenna):
        existing_data = get_tutor_data(id_user)

        if existing_data:
            update_tutor_data(id_user, asignaturas)
        else:
            insert_tutor_data(id_user, asignaturas)

        session['mensaje'] = {'tipo': 'successUpdate', 'contenido': 'Campos actualizados correctamente'}
        return redirect(url_for('profileTutor'))
    else:
        session['mensaje'] = {'tipo': 'errorPassword', 'contenido': 'La contraseña proporcionada es incorrecta. Por favor, inténtalo de nuevo.'}
        return redirect(url_for('profileTutor'))

    return render_template('profileTutor.html', user_profile=user_profile, mensaje=mensaje, longitud=num_notificaciones(), notificaciones=obtener_notificaciones(), tutor=isTutor())

# MANEJO DE EVENTOS PARA FULLCALENDAR
@app.route("/insert",methods=["POST","GET"])
def insert():

    id_user = session['id_user']
    
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        print(title)     
        print(start)  

        cur.execute("INSERT INTO events (id_user, title, start, end) VALUES (%s,%s,%s,%s)",[id_user,title,start,end])
        mysql.connection.commit()       
        cur.close()
        msg = 'success'  
    return jsonify(msg)

@app.route("/update",methods=["POST","GET"])
def update():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        id = request.form['id']
        print(title)     
        print(start)  
        cur.execute("UPDATE events SET title = %s, start = %s, end = %s WHERE id = %s ", [title, start, end, id])
        mysql.connection.commit()       
        cur.close()
        msg = 'success'  
    return jsonify(msg)    
 
@app.route("/ajax_delete",methods=["POST","GET"])
def ajax_delete():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['id']
        print(getid)
        cur.execute('DELETE FROM events WHERE id = {0}'.format(getid))
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'  
    return jsonify(msg) 

# Ruta para subir un archivo
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_data = file.read()

    name = request.form['name']

    query = "INSERT INTO file (name, file) VALUES (%s,%s)"
    cursor = mysql.connection.cursor()
    cursor.execute(query, (name, file_data,))
    mysql.connection.commit()

    return redirect(url_for('archivos'))

# Ruta para descargar un archivo
@app.route('/download', methods=['POST'])
def download_file():
    file_name = request.form['name']

    query = "SELECT file FROM file WHERE name = %s"
    cursor = mysql.connection.cursor()
    cursor.execute(query, (file_name,))
    result = cursor.fetchone()

    file_data = result['file']

    return send_file(
        io.BytesIO(file_data),
        mimetype='application/octet-stream',
        download_name=f"file_{file_name}.pdf",
        as_attachment=True
    )

def create_study_group(request, user_profile):
    try:
        cursor = mysql.connection.cursor()
        title = request.form.get('title')
        subject = request.form.get('subject')
        description = request.form.get('description')
        location = request.form.get('location')
        days = request.form.get('days')
        time = request.form.get('time')

        creator = f"{user_profile['name']} {user_profile['last_name']}"
        creator_mail = user_profile['email']

        cursor = mysql.connection.cursor()
        query = "INSERT INTO study_groups (title, subject, description, location, days, time, name_user, creator_mail) VALUES (%s, %s, %s, %s, %s, %s,  %s,  %s)"
        values = (title, subject, description, location, days, time, creator, creator_mail)
        cursor.execute(query, values)
        mysql.connection.commit()

        # Get the id_group of the newly created group
        cursor.execute("SELECT LAST_INSERT_ID()")
        group_id = cursor.fetchone()[0]

        # Insert the creator's name into the group_participants table
        query = "INSERT INTO group_participants (group_id, user_name) VALUES (%s, %s)"
        values = (group_id, creator)
        cursor.execute(query, values)
        mysql.connection.commit()

        cursor.close()

        flash('Group created successfully', 'success')
        return redirect(url_for('estudio'))

    except Exception as e:
        flash(f'Error creating group: {str(e)}', 'error')
        return redirect(url_for('estudio'))
# Funcion auxiliar para obtener el perfil del usuario


def get_user_profile():
    return {
        'name': session.get('name'),
        'last_name': session['last_name'],
        'email': session['email'],
        'status': session['status'],
        'nombre_grado': session['nombre_grado'],
        'photo_url': 'static/images/userPhoto.png',
        'role': 'Estudiante',
    }

@app.route('/estudio', methods=['GET', 'POST'])
def estudio():
    user_profile = get_user_profile()
    
    if request.method == 'POST':
        return create_study_group(request, user_profile)

    groups_list = fetch_study_groups()
    
    return render_template('estudio.html', user_profile=user_profile, groups=groups_list, longitud=num_notificaciones(), notificaciones=obtener_notificaciones(), tutor = isTutor())

# Funcion auxiliar para obtener los grupos de estudio
def fetch_study_groups():
    
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM study_groups')
    groups = cursor.fetchall()
    cursor.close()

    groups_list = []
    for group in groups:
        id_group = group['id_group']
        title = group['title']
        subject = group['subject']
        description = group.get('description', '')
        location = group['location']
        days = group['days']
        time = group['time']
        creator = group['name_user']
        creator_mail = group['creator_mail']
        participants = fetch_group_participants(group['id_group'])
        group['participants'] = participants

        group_info = {
            'id_group': id_group,
            'title': title,
            'subject': subject,
            'description': description,
            'location': location,
            'days': days,
            'time': time,
            'creator': creator,
            'creator_mail': creator_mail,
            'participants': participants
        }
        groups_list.append(group_info)

    return groups_list

def fetch_group_participants(group_id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT user_name FROM group_participants WHERE group_id = %s', (group_id,))
    participants = [row['user_name'] for row in cursor.fetchall()]
    cursor.close()
    return participants

@app.route('/join_study_group/<int:group_id>', methods=['POST'])
def join_study_group(group_id):
    user_profile = get_user_profile()
    participant = f"{user_profile['name']} {user_profile['last_name']}"

    try:
        cursor = mysql.connection.cursor()
        query = "INSERT INTO group_participants (group_id, user_name) VALUES (%s, %s)"
        values = (group_id, participant)
        cursor.execute(query, values)
        mysql.connection.commit()

        return jsonify(success=True)
    except Exception as e:
        print(str(e))
        return jsonify(success=False, error=str(e))

@app.route('/delete_study_group/<int:group_id>', methods=['DELETE'])
def delete_study_group(group_id):
    try:
        if request.method == 'DELETE':
            cursor = mysql.connection.cursor()
            cursor.execute('DELETE FROM study_groups WHERE id_group = %s', (group_id,))
            mysql.connection.commit()
            cursor.close()

            return jsonify(success=True)
    except Exception as e:
        print(str(e))
        return jsonify(success=False, error=str(e))


# Podcast
@app.route('/podcast')
def podcast(): 

    user_profile = loginfo(session)

    cur = mysql.connection.cursor()
    cur.execute("SELECT name, name_user, description, id_podcast from podcast")
    podcasts_data = cur.fetchall()
    cur.close()
 
    podcasts_list = []
    for podcast in podcasts_data:
        nombre_podcast = podcast['name']
        nombre_usuario = podcast['name_user']
        description = podcast['description']
        id_podcast = podcast['id_podcast']

        podcast_info = {
            'nombre_podcast': nombre_podcast,
            'nombre_usuario': nombre_usuario,
            'id_podcast': id_podcast,
            'description': description
        }
        podcasts_list.append(podcast_info)

    return render_template('podcast.html', user_profile=user_profile, podcasts=podcasts_list, longitud = num_notificaciones(), notificaciones = obtener_notificaciones(), tutor = isTutor())

# PodcastTutor
@app.route('/podcastTutor')
def podcastTutor(): 

    user_profile = loginfo(session)

    cur = mysql.connection.cursor()
    cur.execute("SELECT name, name_user, description, id_podcast from podcast")
    podcasts_data = cur.fetchall()
    cur.close()
 
    podcasts_list = []
    for podcast in podcasts_data:
        nombre_podcast = podcast['name']
        nombre_usuario = podcast['name_user']
        description = podcast['description']
        id_podcast = podcast['id_podcast']

        
        podcast_info = {
            'nombre_podcast': nombre_podcast,
            'nombre_usuario': nombre_usuario,
            'id_podcast': id_podcast,
            'description': description
        }
        podcasts_list.append(podcast_info)

    return render_template('podcastTutor.html', user_profile=user_profile, podcasts=podcasts_list, longitud = num_notificaciones(), notificaciones = obtener_notificaciones(), tutor = isTutor())


# Ruta para subir un archivos mp3
@app.route('/get_audio/<int:id_podcast>')
def get_audio(id_podcast):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT podcast FROM podcast WHERE id_podcast = %s", (id_podcast,))
    audio_data = cursor.fetchone()

    if audio_data:
        audio_filename = 'temp_audio.mp3'
        with open(audio_filename, 'wb') as audio_file:
            audio_file.write(audio_data['podcast'])

        return send_file(audio_filename, as_attachment=True)
    else:
        return "Podcast no encontrado", 404
    
@app.route('/uploadMp3', methods=['POST'])
def upload_mp3():
    name_user = session['name']
    if request.method == 'POST':
        podcast = request.files['podcastFile']
        podcast_data = podcast.read()

        name = request.form['podcastName']
        description = request.form['description']

        query = "INSERT INTO podcast (name, name_user, description, podcast) VALUES (%s,%s,%s,%s)"
        cursor = mysql.connection.cursor()
        cursor.execute(query, (name, name_user, description, podcast_data,))
        mysql.connection.commit()
    return redirect(url_for('podcast'))

@app.route('/subir_audio', methods=['POST'])
def subir_audio():
    name_user = session.get('name')

    if 'audio' not in request.files:
        return "No se encontró el archivo de audio."
    if request.method == 'POST':
            audio = request.files['audio']
            audio_content = audio.read()
            audio_filename = f"{name_user}_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"

            description = request.form.get('description')

            insert_query = "INSERT INTO podcast (name_user, name, description, podcast) VALUES (%s, %s, %s, %s)"
            values = (name_user, audio_filename, description, audio_content,)
            cursor = mysql.connection.cursor()
            cursor.execute(insert_query, values)
            mysql.connection.commit()
    return redirect(url_for('estudio'))

# Archivos disponibles
@app.route('/archivos_disponibles', methods=['GET'])
def mostrar_archivos():
    user_profile = loginfo(session)

    if request.method == 'GET':

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT name FROM file")
        archivos = [archivo['name'] for archivo in cursor.fetchall()]
        return render_template('archivos.html', archivos=archivos, user_profile=user_profile,longitud = num_notificaciones(), notificaciones = obtener_notificaciones(), tutor = isTutor())

    
def obtener_notificaciones():
    tu_id = session['id_user']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id_user,mensaje FROM Tutoria WHERE id_tutor = %s", (tu_id, ))
    notificaciones = cursor.fetchall()
    return notificaciones


def num_notificaciones():
    tu_id = session['id_user']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT count(mensaje) AS conteo FROM Tutoria WHERE id_tutor = %s", (tu_id,))

    result = cursor.fetchone()

    if result is not None:
        num = result['conteo']
        return num
    else:
        return 0
    """ esto nos estaba fastidiando el codigo juan 
    if(num > 9):
        return "+9"
    else:
        return num
    """

#CHATBOT
@app.route("/chatbot")
def chatbot():
    user_profile = {
            'name': session['name'],
            'last_name': session['last_name'],
            'status': session['status']
           
        }
    return render_template('chatbot.html', user_profile=user_profile, longitud = num_notificaciones(), notificaciones = obtener_notificaciones(), tutor = isTutor())

@app.route("/chatbotTutor")
def chatbotTutor():
    user_profile = {
            'name': session['name'],
            'last_name': session['last_name'],
            'status': session['status']
           
        }
    return render_template('chatbotTutor.html', user_profile=user_profile, longitud = num_notificaciones(), notificaciones = obtener_notificaciones(), tutor = isTutor())


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    if not msg:
        return jsonify({"error": "El mensaje está vacío"}), 400
    input = msg
    chat_messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': input}]
    return get_openai_response(chat_messages)

def get_openai_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
    )

    return response['choices'][0]['message']['content']

@app.route("/get_welcome_message", methods=["POST"])
def get_welcome_message():
    user_name = session.get('name', 'Usuario')
    welcome_message = f"Bienvenido, {user_name} ¿En qué puedo ayudarte?"
    return welcome_message


#JARVIS
@app.route("/jarvis")
def jarvis():
    user_profile = {
            'name': session['name'],
            'last_name': session['last_name'],
            'status': session['status']
           
        }
    return render_template('jarvis.html', user_profile=user_profile, longitud = num_notificaciones(), notificaciones = obtener_notificaciones(), tutor = isTutor())

@app.route('/ask', methods=['POST'])
def ask_assistant():
    data = request.json
    user_input = data.get('input')

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=100
    )

    return jsonify({'response': response['choices'][0]['text']})

def isTutor():
    if(session['status'] == 'Tutor'):
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(debug=True)
