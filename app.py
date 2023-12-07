from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file, jsonify
from flask_mysqldb import MySQL, MySQLdb
from datetime import datetime
import io
import base64
import json
import binascii
from datetime import datetime
from Contact import loginfo, crearDirectorio
import openai
from dotenv import load_dotenv
import os

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
        # Obtén los datos del formulario de inicio de sesión
        email = request.form['email']
        contrasenna = request.form['password']

        # Crea un cursor para interactuar con la base de datos
        cur = mysql.connection.cursor()

        # Obtiene la contraseña almacenada para el usuario
        cur.execute("SELECT id_user, contrasenna, nombre, apellido, status, nombre_grado FROM user WHERE eMail = %s", [email])
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
            session['id_user'] = result['id_user']
            session['name'] = result['nombre']
            session['last_name'] = result['apellido']
            session['status'] = result['status']
            session['nombre_grado'] = result['nombre_grado']
        
            if session['status'] == 'Tutor':
                return redirect(url_for('dashboardTutor'))
            else:
                return redirect(url_for('dashboard'))
            
        else:
        # Contraseña incorrecta
            flash('Email o contraseña incorrectos', 'error')

    return render_template('login.html', error=error)

#DashBoard
@app.route('/dashboard')
def dashboard():

    id_user = session['id_user']
    
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM events WHERE id_user = %s ORDER BY id", (id_user,))
    calendar = cur.fetchall()  

    user_profile = loginfo(session)

    return render_template('dashboard.html', user_profile=user_profile, calendar=calendar, longitud = num_notificaciones(), notificaciones = obtener_notificaciones())


#Tables
@app.route('/tables')
def tables():
    user_profile = loginfo(session)
    return render_template('tables.html', user_profile=user_profile, longitud = num_notificaciones(), notificaciones = obtener_notificaciones())

#TablesTutor
@app.route('/tablesTutor')
def tablesTutor():
    user_profile = loginfo(session)
    return render_template('tablesTutor.html', user_profile=user_profile, longitud = num_notificaciones(), notificaciones = obtener_notificaciones())
 
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
    #Obtenemos la informacion del usuario
    user_profile = loginfo(session)
    #Creamos el directorio de imagenes
    crearDirectorio(ruta)

    #Creamos la conexion a la base de datos
    cur = mysql.connection.cursor()

    #Parte del codigo que destruye las imagenes
    archivos = os.listdir(ruta)
    archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(ruta, archivo))]
    cont_fotos = len(archivos)

    if(cont_fotos > 0):
        for i in range(0,cont_fotos-1):
            temp_image_path = f'static/Fotos_Tutor/temp_image{i}.jpg'
            if os.path.exists(temp_image_path):
                os.remove(temp_image_path)
        print("Imagenes borradas")


    #Codigo para obetener los datos de cada tutor
    cur.execute("SELECT * FROM vista_ventana_tutores")
    contacts = cur.fetchall()
    cur.close()

    #Parte del codigo que tranforma las imagenes para verse en el html
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

                # Decodifica los datos base64 en una representación de bytes
                image_data = base64.b64decode(image_data_hex)

                # Crea un archivo temporal para almacenar la imagen
                with open(f'static/Fotos_Tutor/temp_image{cont}.jpg', 'wb') as f:
                    f.write(image_data)

                image_base64 = f"static/Fotos_Tutor/temp_image{cont}.jpg";

                cont = cont + 1

            except binascii.Error:
                # Si hay un error al decodificar, puedes manejarlo de acuerdo a tus necesidades
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

        #Para que no salgas en la lista de tutores si estas en tu sesion
        if contact['nombre_apellido'] != isUser:
            contacts_list.append(contact)

    return render_template('contact.html', contacts=contacts_list, user_profile=user_profile, longitud = num_notificaciones(), notificaciones = obtener_notificaciones())


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


#Tutelados
@app.route('/tutelados')
def tutelados():
    user_profile = loginfo(session)
    return render_template('tutelados.html', user_profile=user_profile)

@app.route('/profile')
def profile():
    # Fetch user's profile information from your data source (e.g., session, database)
    user_profile = None
    user_profile = {
        'name': session.get('name'),
        'last_name': session['last_name'],
        'email': session['email'],
        'status': session['status'],
        'nombre_grado': session['nombre_grado'],
        'photo_url': 'static/images/userPhoto.png',  # Replace with the actual URL of the user's photo
        'role': 'Estudiante',  # Replace with the actual user's role
    }
    mensaje = session.pop('mensaje', None)
    

    return render_template('profile.html', user_profile=user_profile, mensaje=mensaje, longitud = num_notificaciones(), notificaciones = obtener_notificaciones())

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
        'photo_url': 'static/images/userPhoto.png',  # Replace with the actual URL of the user's photo
        'role': 'Estudiante',  # Replace with the actual user's role
    }
    mensaje = session.pop('mensaje', None)

    return render_template('profileTutor.html', user_profile=user_profile, mensaje=mensaje, longitud = num_notificaciones(), notificaciones = obtener_notificaciones())

# Dashboard Tutor
@app.route('/dashboardTutor')
def dashboardTutor():

    id_user = session['id_user']
    
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM events WHERE id_user = %s ORDER BY id", (id_user,))
    calendar = cur.fetchall()  

    user_profile = None
    if 'logged_in' in session:
        user_profile = {
            'name': session['name'],
            'last_name': session['last_name'],
            'email': session['email'],
            'status': session['status']
        }
    mensaje1 = session.pop('mensaje1', None)
 
    return render_template('dashboardTutor.html', user_profile=user_profile, mensaje1=mensaje1, calendar=calendar, longitud = num_notificaciones(), notificaciones = obtener_notificaciones())

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
        grado = request.form['grado']

        user_profile = {
            'name': session['name'],
            'last_name': session['last_name'],
            'status': session['status'],
            'email': session['email'],
            'nombre_grado': session['nombre_grado']
           
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
                cursor.execute("UPDATE user SET nombre = %s, apellido = %s, eMail = %s, nombre_grado= %s WHERE contrasenna = %s", [nombre, apellido, email, grado, contrasenna])
                mysql.connection.commit()
                cursor.close()

                session['name'] = nombre
                session['last_name'] = apellido
                session['email'] = email
                session['nombre_grado'] = grado

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
        #else:
         #   session['mensaje'] = {'tipo':'error','contenido':'imagen no actualizada'}
          #  return redirect(url_for('profile')) 

        
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
        return "Imagen no encontrada", 404 


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
                return redirect(url_for('profile'))
            else:
                session['mensaje'] = {'tipo': 'errorPassword', 'contenido': 'Los campos Nueva contraseña y Confirmar contraseña no coinciden. Por favor, inténtalo de nuevo.'}
                return redirect(url_for('profile'))
        else:
            session['mensaje'] = {'tipo': 'errorPassword', 'contenido': 'La contraseña proporcionada es incorrecta. Por favor, inténtalo de nuevo.'}
            return redirect(url_for('profile')) 
        
    return render_template('profile.html', user_profile=user_profile, mensaje=mensaje)

#Darse de alta de tutor
@app.route('/altaTutor',  methods=['GET', 'POST'])
def altaTutor():
     
     user_profile = None
     mensaje1 = None
     
     if request.method == 'POST':
    
        email_from_session = session["email"]
        contrasenna = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT contrasenna FROM user WHERE eMail = %s", [email_from_session])
        result = cur.fetchone()

        if result['contrasenna'] == contrasenna:
                id_tutor = session["id_user"]
                cursor = mysql.connection.cursor()
                cursor.execute("UPDATE user SET status = 'Tutor' WHERE contrasenna = %s", [contrasenna])
                cursor.execute("INSERT INTO tutor (id_tutor) VALUES(%s)", [id_tutor])
                result = cursor.fetchone()
                mysql.connection.commit()


                cursor2 = mysql.connection.cursor()
                cursor2.execute("SELECT status FROM user WHERE eMail = %s", [email_from_session])
                resultado = cursor2.fetchone()
                mysql.connection.commit()
                session['status'] = resultado['status']

                session['mensaje1'] = {'tipo':'successUpdate','contenido':'Te has dado de alta como Tutor'}
                return redirect(url_for('dashboardTutor'))     
        else:
            session['mensaje1'] = {'tipo': 'errorPassword', 'contenido': 'La contraseña proporcionada es incorrecta. Por favor, inténtalo de nuevo.'}
            return redirect(url_for('profile')) 
        
     return render_template('profile.html', user_profile=user_profile, mensaje1=mensaje1)

#Cambiar campos de tutor
@app.route('/camposTutor', methods=['GET', 'POST'])
def campos_tutor():

    user_profile = None
    mensaje = None

    if request.method == 'POST':
    
     contrasenna = request.form['password']
     tarifa = request.form['tarifa']
     asignaturas = request.form['asignaturas']
     email_from_session = session["email"]
     id_user = session["id_user"]
     
     cur = mysql.connection.cursor()
     cur.execute("SELECT contrasenna FROM user WHERE eMail = %s", [email_from_session])
     result = cur.fetchone()

     if result['contrasenna'] == contrasenna:

        # Comprobar si ya existen registros para este usuario
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM tutor WHERE id_tutor = %s", (id_user,))
            existing_data = cursor.fetchone()

            if existing_data:
                # Si ya existen datos, realizar una actualización
                cursor.execute("UPDATE tutor SET tarifa = %s, asignaturas_tutor = %s WHERE id_tutor = %s", (tarifa, asignaturas, id_user))
                mysql.connection.commit()
                cursor.close()

                session['mensaje'] = {'tipo': 'successUpdate', 'contenido': 'Campos actualizados correctamente'}
                return redirect(url_for('profileTutor'))

            else:
                # Si no existen datos, realizar una inserción
                cursor.execute("INSERT INTO tutor (id_tutor,tarifa, asignaturas_tutor) VALUES (%s,%s, %s)", (id_user,tarifa, asignaturas))
                mysql.connection.commit()
                cursor.close()

                session['mensaje'] = {'tipo': 'successUpdate', 'contenido': 'Campos actualizados correctamente'}
                return redirect(url_for('profileTutor'))
    else:
        session['mensaje'] = {'tipo': 'errorPassword', 'contenido': 'La contraseña proporcionada es incorrecta. Por favor, inténtalo de nuevo.'}
        return redirect(url_for('profileTutor'))
    
    return render_template('profileTutor.html', user_profile=user_profile, mensaje=mensaje)

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

    return redirect(url_for('tables'))

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

@app.route('/estudio', methods=['GET', 'POST'])
def estudio():

    # Obtener los datos del usuario
    user_profile = {
        'name': session.get('name'),
        'last_name': session['last_name'],
        'email': session['email'],
        'status': session['status'],
        'nombre_grado': session['nombre_grado'],
        'photo_url': 'static/images/userPhoto.png'
    }

    if request.method == 'POST':
        # Obtener los datos del formulario
        titulo = request.form.get('title')
        asignatura = request.form.get('subject')
        descripcion = request.form.get('description')
        ubicacion = request.form.get('location')
        dias = request.form.get('days')
        hora = request.form.get('time')

        creador = user_profile['name'] + " " + user_profile['last_name']

        # Obtener el archivo de imagen
        # photo = request.files['photo']
        #photo_data = photo.read()

        # Guardar la información del grupo en la base de datos
        query = "INSERT INTO study_prueba (title, subject, description, location, days, time, name_user) VALUES (%s, %s, %s, %s, %s, %s,  %s)"
        values = (titulo, asignatura, descripcion, ubicacion, dias, hora, creador)
        cursor = mysql.connection.cursor()
        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('estudio'))

    cursor = mysql.connection.cursor()
    # Fetch events from the 'studio' table
    cursor.execute('SELECT * FROM study_prueba')
    groups = cursor.fetchall()
    cursor.close()

    # Obtener los grupos de estudio de la base de datos
    groups_list = []
    for group in groups:
        titulo = group[0]
        asignatura = group[1]
        descripcion = group[2]
        ubicacion = group[3]
        dias = group[4]
        hora = group[5]
        creador = group[6]

        group_info = {
            'titulo': titulo,
            'asignatura': asignatura,
            'descripcion': descripcion,
            'ubicacion': ubicacion,
            'dias': dias,
            'hora': hora,
            'creador': creador
        }
        groups_list.append(group_info)

    return render_template('estudio.html', user_profile=user_profile, groups  = groups_list, longitud = num_notificaciones(), notificaciones = obtener_notificaciones())

@app.route('/estudioTutor', methods=['GET', 'POST'])
def estudioTutor():
    user_profile = {
        'name': session.get('name'),
        'last_name': session['last_name'],
        'email': session['email'],
        'status': session['status'],
        'nombre_grado': session['nombre_grado'],
        'photo_url': 'static/images/userPhoto.png',
        'role': 'Estudiante',
    }

    # Obtener los datos del formulario
    titulo = request.form.get('title')
    asignatura = request.form.get('subject')
    descripcion = request.form.get('description')
    ubicacion = request.form.get('location')
    # creador = user_profile['name']
    dias = request.form.get('days')
    hora = request.form.get('time')

    # Obtener el archivo de imagen
    # photo = request.files['photo']
    #photo_data = photo.read()

    # Guardar la información del grupo en la base de datos
    query = "INSERT INTO study_prueba (title, subject, description, location, days, time) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (titulo, asignatura, descripcion, ubicacion, dias, hora)
    cursor = mysql.connection.cursor()
    cursor.execute(query, values)
    mysql.connection.commit()

    # Fetch events from the 'studio' table
    cursor.execute('SELECT * FROM study_prueba')
    groups = cursor.fetchall()
    cursor.close()

    # Obtener los grupos de estudio de la base de datos
    groups_list = []
    for group in groups:
        titulo = group['title']
        asignatura = group['subject']
        descripcion = group['description']
        ubicacion = group['location']
        dias = group['days']
        hora = group['time']
        creador: user_profile['name']


        group_info = {
            'titulo': titulo,
            'asignatura': asignatura,
            'descripcion': descripcion,
            'ubicacion': ubicacion,
            'dias': dias,
            'hora': hora,
            'creador': creador
        }
        groups_list.append(group_info)

    return render_template('estudioTutor.html', user_profile=user_profile, groups=groups_list, longitud = num_notificaciones(), notificaciones = obtener_notificaciones())


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
            # Puedes agregar más campos del podcast si los necesitas
        }
        podcasts_list.append(podcast_info)

    return render_template('podcast.html', user_profile=user_profile, podcasts=podcasts_list, longitud = num_notificaciones(), notificaciones = obtener_notificaciones())

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
            # Puedes agregar más campos del podcast si los necesitas
        }
        podcasts_list.append(podcast_info)

    return render_template('podcastTutor.html', user_profile=user_profile, podcasts=podcasts_list, longitud = num_notificaciones(), notificaciones = obtener_notificaciones())



# Ruta para subir un archivos mp3
@app.route('/get_audio/<int:id_podcast>')
def get_audio(id_podcast):
    # Obtén el archivo de audio desde la base de datos utilizando el podcast_id
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT podcast FROM podcast WHERE id_podcast = %s", (id_podcast,))
    audio_data = cursor.fetchone()

    if audio_data:
        # Guarda el audio en un archivo temporal
        audio_filename = 'temp_audio.mp3'
        with open(audio_filename, 'wb') as audio_file:
            audio_file.write(audio_data['podcast'])

        # Devuelve el archivo de audio al navegador
        return send_file(audio_filename, as_attachment=True)
    else:
        # Manejar el caso donde el podcast no existe
        return "Podcast no encontrado", 404
    
@app.route('/uploadMp3', methods=['POST'])
def upload_mp3():
    name_user = session['name']

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

    audio = request.files['audio']

    # Lee el contenido del archivo como bytes
    audio_content = audio.read()

    # Genera un nombre único para el archivo de audio
    audio_filename = f"{name_user}_{datetime.now().strftime('%Y%m%d%H%M%S')}.wav"

    # Obtén la descripción del formulario
    description = request.form.get('description')

    # Guarda la información del audio en la base de datos
    insert_query = "INSERT INTO podcast (name_user, name, description, podcast) VALUES (%s, %s, %s, %s)"
    values = (name_user, audio_filename, description, audio_content,)
    cursor = mysql.connection.cursor()
    cursor.execute(insert_query, values)
    mysql.connection.commit()

    return "Audio subido exitosamente."

# Archivos disponibles
@app.route('/archivos_disponibles', methods=['GET'])
def mostrar_archivos():
    user_profile = loginfo(session)

    if request.method == 'GET':

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT name FROM file")
        archivos = [archivo['name'] for archivo in cursor.fetchall()]
        return render_template('tables.html', archivos=archivos, user_profile=user_profile)
    
def obtener_notificaciones():
    tu_id = session['id_user']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT mensaje FROM Tutoria WHERE id_tutor = %s", (tu_id, ))
    notificaciones = cursor.fetchall()
    print("estoy en obtener_Notificaciones")
    return notificaciones


def num_notificaciones():
    tu_id = session['id_user']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT count(mensaje) AS conteo FROM Tutoria WHERE id_tutor = %s", (tu_id,))

    result = cursor.fetchone()
    # num = cursor.fetchone()['conteo']

    if result is not None:
        num = result['conteo']
        return num
    else:
        # Handle the case where result is None, e.g., set a default value or raise an exception.
        return 0  # Default value, adjust as needed

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
    return render_template('chatbot.html', user_profile=user_profile)

@app.route("/chatbotTutor")
def chatbotTutor():
    user_profile = {
            'name': session['name'],
            'last_name': session['last_name'],
            'status': session['status']
           
        }
    return render_template('chatbotTutor.html', user_profile=user_profile)


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
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
    return render_template('jarvis.html', user_profile=user_profile)

@app.route('/ask', methods=['POST'])
def ask_assistant():
    data = request.json
    user_input = data.get('input')


    # Lógica para procesar 'user_input' y enviar la solicitud a la API de OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=100
    )

    return jsonify({'response': response['choices'][0]['text']})


if __name__ == '__main__':
    app.run(debug=True)
