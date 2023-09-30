from PyQt5 import QtCore, QtGui, QtWidgets
from email.mime import image
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
from tkinter import filedialog

def show_student_profile():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    contraseña = contraseña_entry.get()
    email = email_entry.get()
    grado = grado_entry.get()

    profile_label.config(text=f" {nombre}\n\n {apellido}\n\n {grado}\n\n {contraseña}\n\n {email}")

def choose_image():
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    image.thumbnail((100, 100))
    photo = ImageTk.PhotoImage(image)
    profile_image_label.config(image=photo)
    profile_image_label.image = photo

root = tk.Tk()
root.title("Student Profile")

# nombre
nombre_label = tk.Label(root, text="Nombre:")
nombre_label.grid(row=2, column=0, sticky="e")

nombre_entry = tk.Entry(root)
nombre_entry.grid(row=2, column=1)

# Last nombre
apellido_label = tk.Label(root, text="Apellido:")
apellido_label.grid(row=3, column=0, sticky="e")

apellido_entry = tk.Entry(root)
apellido_entry.grid(row=3, column=1)

# Email
email_label = tk.Label(root, text="Email:")
email_label.grid(row=6, column=0, sticky="e")

email_entry = tk.Entry(root)
email_entry.grid(row=6, column=1)

# Contraseña
contraseña_label = tk.Label(root, text="Contraseña:")
contraseña_label.grid(row=4, column=0)

contraseña_entry = tk.Entry(root)
contraseña_entry.grid(row=4, column=1)

# Grado
grado_label = tk.Label(root, text="Grado:")
grado_label.grid(row=5, column=0, sticky="e")

grado_entry = tk.Entry(root)
grado_entry.grid(row=5, column=1)

# Profile Image
image_button = tk.Button(root, text="Choose Image", command=choose_image)
image_button.grid(row=1, column=0, columnspan=2, rowspan=1)

profile_image_label = tk.Label(root)
profile_image_label.grid(row=0, column=0, columnspan=2)

# Show Profile Button
show_profile_button = tk.Button(root, text="guardar",command=show_student_profile)
show_profile_button.grid(row=8, column=0, columnspan=2)

# Profile Label
profile_label = tk.Label(root)
profile_label.grid(row=0, column=4, ipadx=30, ipady=30)

# Crear la etiqueta para mostrar los datos
etiqueta = tk.Label(root, text="Nombre: \n\nApellido: \n\nGrado: \n\nContraseña: \n\nEmail: ")
etiqueta.grid(row=0, column=3)

root.mainloop()