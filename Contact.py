
#Método para crear un Directorio si no existe
def crearDirectorio(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)

def loginfo():
    if 'logged_in' in session:
        {
            'name': session['name'],
            'last_name': session['last_name'],
            'status' : session['status']
        }
    else:
        None
