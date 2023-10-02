# Importa la clase DatabaseConnection desde el archivo correcto
from DataBaseConnection import DatabaseConnection

# Crea una instancia de DatabaseConnection con la configuración adecuada
db = DatabaseConnection(
    host="uni-connect.mysql.database.azure.com",
    user="XMoraP",
    port=3306,
    password="12345678u$",
    database="uniconnect",
    ssl_ca="./DigiCertGlobalRootCA.crt.pem",
    ssl_disabled=False
)

# Realiza una consulta SELECT en la tabla "user" (ajusta el nombre de la tabla según tu base de datos)
select_query = "SELECT * FROM user"
data = db.fetch_data(select_query)

# Verifica si se obtuvieron datos y muestra los resultados
if data:
    for row in data:
        print(row)

# Cierra la conexión
db.close_connection()
