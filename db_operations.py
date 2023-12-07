# Function to obtain notifications from the database
def obtener_notificaciones():
    tu_id = session['id_user']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT mensaje FROM Tutoria WHERE id_tutor = %s", (tu_id,))
    notificaciones = cursor.fetchall()
    print("estoy en obtener_Notificaciones")
    return notificaciones

# Function to get the number of notifications
def num_notificaciones():
    tu_id = session['id_user']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT count(mensaje) AS conteo FROM Tutoria WHERE id_tutor = %s", (tu_id,))
    num = cursor.fetchone()['conteo']
    if(num > 9):
        return "+9"
    else:
        return num
