import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.principal import Ui_Form
from ui.login import Ui_ContainerLogin
from ui.register import Ui_containerRegister
import ui.imagenes.resorces_rc
from db_connection.DataBaseConnection import DatabaseConnection

class RegisterWindow(QMainWindow, Ui_containerRegister):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db_connection = db_connection  # Store the database connection

        # Connect the "Aceptar" button's click event to the registration function
        self.botonAceptarRegister.clicked.connect(self.register_user)

    def register_user(self):
        try:
            # Retrieve user input from the registration form
            email = self.cajaEmailRegister.text()
            password = self.cajaContrasennaRegister.text()
            username = self.cajaUsuarioRegister.text()
            nombre, apellido = username.split(" ")



            # Check if email and password are not empty
            if email and password and username:
                try:
                    # Create a cursor to execute SQL queries
                    cursor = self.db_connection.cursor()

                    # Define the INSERT query to add the user to the 'user' table
                    insert_query = f"INSERT INTO user (eMail, contrasenna, nombre, apellido) VALUES ('{email}', '{password}', '{nombre}', '{apellido}')"

                    # Execute the query
                    cursor.execute(insert_query)

                    # Commit the changes to the database
                    self.db_connection.commit()

                    # Display a success message
                    print("User registered successfully.")

                    # Close the cursor
                    cursor.close()

                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                    self.db_connection.rollback()
            else:
                print("Email and password fields cannot be empty.")

        except Exception as e :
            print(e)

class LoginWindow(QMainWindow, Ui_ContainerLogin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect the "Registrate" button's click event to open the registration window and close the login window
        self.enlaceRegistrate.clicked.connect(self.open_register_window)

    def open_register_window(self):
        self.close()  # Close the login window
        self.register_window = RegisterWindow()
        self.register_window.show()  # Show the registration window

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.iniciarsesion.clicked.connect(self.open_login_window)

    def open_login_window(self):
        self.close()
        self.login_window = LoginWindow()
        self.login_window.show()

if __name__ == "__main__":
    # Establish a MySQL database connection
    db_connection = mysql.connector.connect(
        host="uni-connect.mysql.database.azure.com",
        user="XMoraP",
        password="12345678u$",
        database="uniconnect"
    )

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
