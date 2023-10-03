import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.principal import Ui_main
from ui.login import Ui_ContainerLogin
from ui.register import Ui_containerRegister
#import ui.imagenes.resorces_rc
#from db_connection.DataBaseConnection import DatabaseConnection
from ui.home import Ui_ContainerHome
from ui.editProfile import Ui_containerEditProfile
from ui.editProfileTutor import Ui_containerEditProfileTutor

class EditProfileTutorWindow(QMainWindow, Ui_containerEditProfileTutor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.exitButton.clicked.connect(self.close)
        self.homeButton.clicked.connect(self.open_home_window)
        self.userButton.clicked.connect(self.open_profile_window)
    def open_home_window(self):
        self.close()
        self.home_window = HomeWindow()
        self.home_window.show()

    def open_profile_window(self):
        self.close()
        self.profile_window = EditProfileWindow()
        self.profile_window.show()

class EditProfileWindow(QMainWindow, Ui_containerEditProfile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tutorButton.clicked.connect(self.open_tutor_profile_window)
        self.exitButton.clicked.connect(self.close)
        self.homeButton.clicked.connect(self.open_home_window)

    def open_tutor_profile_window(self):
        self.close()
        self.tutor_window = EditProfileTutorWindow()
        self.tutor_window.show()

    def open_home_window(self):
        self.close()
        self.home_window = HomeWindow()
        self.home_window.show()

class HomeWindow(QMainWindow, Ui_ContainerHome):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.homeButton.clicked.connect(self.open_profile_window)
        self.exitButton.clicked.connect(self.close)

    def open_profile_window(self):
        self.close()
        self.profile_window = EditProfileWindow()
        self.profile_window.show()

class RegisterWindow(QMainWindow, Ui_containerRegister):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db_connection = db_connection  # Store the database connection

        self.botonAceptarRegister.clicked.connect(self.register_user)
        self.linkInicioSesionRegister.clicked.connect(self.open_login_window)
        self.iconoVolverAtrasRegister.clicked.connect(self.open_welcome_window)

    def register_user(self):
        try:
            # Retrieve user input from the registration form
            email = self.cajaEmailRegister.text()
            contrasenna = self.cajaContrasennaRegister.text()
            username = self.cajaUsuarioRegister.text()
            nombre, apellido = username.split(" ") #Crea el nombre y apellido a partir del username



            # Check if email and password are not empty
            if email and contrasenna and nombre and apellido:
                try:
                    # Create a cursor to execute SQL queries
                    cursor = self.db_connection.cursor()
                    #Comrobacion de username en la DB
                    query_username = "SELECT count(*) FROM user WHERE nombre = %s AND apellido = %s AND contrasenna = %s"
                    cursor.execute(query_username, (nombre, apellido, contrasenna))
                    result_username = cursor.fetchone()
                    #Comprobar el email en la DB
                    query_email = "SELECT count(*) FROM user WHERE eMail = %s"
                    cursor.execute(query_email, (email,))
                    result_email = cursor.fetchone()
                    if result_username[0] == 0 and result_email == 0:
                        # Define the INSERT query to add the user to the 'user' table
                        insert_query = f"INSERT INTO user (eMail, contrasenna, nombre, apellido) VALUES ('{email}', '{contrasenna}', '{nombre}', '{apellido}')"

                        # Execute the query
                        cursor.execute(insert_query)

                        # Commit the changes to the database
                        self.db_connection.commit()

                        # Display a success message
                        print("User registered successfully.")

                        # Close the cursor
                        cursor.close()
                    else:
                        if(result_email[0] != 0):
                            QMessageBox.critical(self, "Error", "Ese email ya esta asociado a una cuenta")
                        if(result_username[0] != 0):
                            QMessageBox.critical(self, "Error","Ya estas registrado")
                        self.open_login_window()

                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                    self.db_connection.rollback()
            else:
                print("Email and password fields cannot be empty.")

        except Exception as e :
            print(e)
    def open_login_window(self):
        self.close()  # Close the login window
        self.login_window = LoginWindow()
        self.login_window.show()  # Show the registration window
        self.open_home_window()

    def open_home_window(self):
        self.close()
        self.home_window = HomeWindow()
        self.home_window.show()

    def open_login_window(self):
        self.close()
        self.login_window = LoginWindow()
        self.login_window.show()

    def open_welcome_window(self):
        self.close()
        self.welcome_window = MainWindow()
        self.welcome_window.show()


class LoginWindow(QMainWindow, Ui_ContainerLogin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.db_connection = db_connection

        self.enlaceRegistrate.clicked.connect(self.open_register_window)
        self.botonAceptarLogin.clicked.connect(self.iniciar_sesion)
        self.iconoVolverAtrasLogin.clicked.connect(self.open_welcome_window)


    def iniciar_sesion(self):
        try:
            nombre_apellido = self.cajaUsuarioLogin.text().split(" ")
            contrasenna = self.cajaContrasennaLogin.text()
            cursor = self.db_connection.cursor()
            query = "SELECT count(*) FROM user WHERE nombre = %s AND apellido = %s AND contrasenna = %s"
            cursor.execute(query, (nombre_apellido[0], nombre_apellido[1], contrasenna))
            result = cursor.fetchone()  # Fetch one row
            cursor.close()  # Close the cursor
            print(result)
            if result:
                if result[0] == 1:
                    self.open_home_window()
                    print("Has iniciado sesión")
                elif result[0] > 1:
                    print("WTF")
                elif result[0] == 0:
                    reply = QMessageBox.question(self, "No tienes un usuario", "¿Quieres crearlo?",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        self.open_register_window()
        except Exception as e:
            print(e)

    def open_register_window(self):
        self.close()
        self.register_window = RegisterWindow()
        self.register_window.show()

    def open_welcome_window(self):
        self.close()
        self.welcome_window = MainWindow()
        self.welcome_window.show()

    def open_home_window(self):
            self.close()
            self.home_window = HomeWindow()
            self.home_window.show()

class MainWindow(QMainWindow, Ui_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginButton.clicked.connect(self.open_login_window)

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
