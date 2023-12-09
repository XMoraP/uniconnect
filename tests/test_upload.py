from flask.testing import FlaskClient
import pytest
import sys
import os
from unittest.mock import patch, Mock
from flask import Flask
from dotenv import load_dotenv
from flask_mysqldb import MySQL
import os
from unittest.mock import patch, Mock
from flask import Flask
from flask.testing import FlaskClient
from io import BytesIO
import pytest
load_dotenv()

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client
#Test sin el mismo nombre a la base de datos 
def test_upload_file(client):
    # Crear un objeto Mock para representar la conexión a la base de datos
    mock_database = Mock()

    # Decorar la función de prueba para reemplazar la llamada real a la base de datos con el Mock
    with patch('flask_mysqldb.MySQL.connection', mock_database):
        # Configurar el comportamiento esperado del Mock (simular un resultado de la base de datos)
        mock_cursor = mock_database.cursor.return_value
        mock_cursor.fetchone.return_value = None  # Simula que no existe ningún archivo con el mismo nombre

        # Simular una solicitud POST con datos de carga de archivo
        file_content = b"Contenido del archivo"
        file = BytesIO(file_content)
        response = client.post('/upload', data=dict(
        name='Archivo1',  # Nombre del archivo
        file=(BytesIO(file_content), 'test.txt')  # Tupla para representar el campo de archivo
        ))
    
        # Verificar que la respuesta sea exitosa (código 302 ya que redirige)
        assert response.status_code == 302





# Test para cuando se solicita la descarga de un archivo existente en la base de datos
def test_download_file(client):
    # Crear un objeto Mock para representar la conexión a la base de datos
    mock_database = Mock()

    # Decorar la función de prueba para reemplazar la llamada real a la base de datos con el Mock
    with patch('flask_mysqldb.MySQL.connection', mock_database):
        # Configurar el comportamiento esperado del Mock (simular un resultado de la base de datos)
        mock_cursor = mock_database.cursor.return_value
        mock_cursor.fetchone.return_value = {'file': b"Contenido del archivo"}  # Simula el resultado de la base de datos

        # Simular una solicitud POST con el nombre del archivo
        response = client.post('/download', data=dict(
            name='Archivo1',  # Nombre del archivo
        ))

        # Verificar que la respuesta sea exitosa (código 200)
        assert response.status_code == 200

        # Verificar que el contenido de la respuesta sea el mismo que el contenido simulado del archivo
        assert response.data == b"Contenido del archivo"

#Test que asegura de que la app coga la solicitud y descarga archivo y la verificacion

def test_download2_file(client):
    # Crear un objeto Mock para representar la conexión a la base de datos
    mock_database = Mock()

    # Decorar la función de prueba para reemplazar la llamada real a la base de datos con el Mock
    with patch('flask_mysqldb.MySQL.connection', mock_database):
        # Configurar el comportamiento esperado del Mock (simular un resultado de la base de datos)
        mock_cursor = mock_database.cursor.return_value
        mock_cursor.fetchone.return_value = {'file': b"Contenido del archivo"}  # Simula el resultado de la base de datos

        # Simular una solicitud POST con el nombre del archivo
        response = client.post('/download', data=dict(
            name='Archivo1',  # Nombre del archivo
        ))

        # Verificar que la respuesta sea exitosa (código 200)
        assert response.status_code == 200

        # Verificar que el contenido de la respuesta sea el mismo que el contenido simulado del archivo
        assert response.data == b"Contenido del archivo"

        # Verificar que el encabezado de la respuesta contiene la información de descarga
        assert response.headers['Content-Disposition'] == 'attachment; filename=file_Archivo1.pdf'