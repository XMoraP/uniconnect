import mysql.connector

class DatabaseConnection:
    def __init__(self, host, port, user, password, database, ssl_ca, ssl_disabled):
        self.connection = mysql.connector.connect(
            host="uni-connect.mysql.database.azure.com",
            user="XMoraP",
            port=3306,
            password="12345678u$",
            database="uniconnect",
            ssl_ca="./DigiCertGlobalRootCA.crt.pem", 
            ssl_disabled=False
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            self.connection.rollback()
            return False

    def fetch_data(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            return None

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

# Ejemplo de uso de la clase DatabaseConnection
if __name__ == "__main__":
    db = DatabaseConnection(host="localhost", user="tu_usuario", password="tu_contraseña", database="tu_base_de_datos")

    # Ejemplo de ejecución de una consulta INSERT
    """"
    insert_query = "INSERT INTO mi_tabla (campo1, campo2) VALUES ('valor1', 'valor2')"
    if db.execute_query(insert_query):
        print("Inserción exitosa.")
    else:
        print("Error en la inserción.")
"""

