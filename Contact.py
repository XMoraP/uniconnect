import os

#Método para crear un Directorio si no existe
def crearDirectorio(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)

def loginfo(session):
    user_profile = None

    if session['logged_in']:
        user_profile = {
            'name': session['name'],
            'last_name': session['last_name'],
            'status' : session['status']
        }

    return user_profile
