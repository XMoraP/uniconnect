import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow
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

class EditProfileWindow(QMainWindow, Ui_containerEditProfile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tutorButton.clicked.connect(self.open_tutor_profile_window)
        self.exitButton.clicked.connect(self.close)

    def open_tutor_profile_window(self):
        self.close()
        self.tutor_window = EditProfileTutorWindow()
        self.tutor_window.show()

class HomeWindow(QMainWindow, Ui_ContainerHome):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.homeButton.clicked.connect(self.open_profile_window)
        self.exitButton.clicked.connect(self.close)

    def open_profile_window(self):
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
        # Retrieve user input from the registration form
        email = self.cajaEmailRegister.text()
        password = self.cajaContrasennaRegister.text()

        # Check if email and password are not empty
        if email and password:
            try:
                # Create a cursor to execute SQL queries
                cursor = self.db_connection.cursor()
                # Define the INSERT query to add the user to the 'user' table
                insert_query = f"INSERT INTO user (eMail, contrasenna) VALUES ('{email}', '{password}')"
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

        self.enlaceRegistrate.clicked.connect(self.open_register_window)
        self.iconoVolverAtrasLogin.clicked.connect(self.open_welcome_window)

    def open_register_window(self):
        self.close()
        self.register_window = RegisterWindow()
        self.register_window.show()

    def open_welcome_window(self):
        self.close()
        self.welcome_window = MainWindow()
        self.welcome_window.show()



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
