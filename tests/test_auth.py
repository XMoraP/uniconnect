from flask.testing import FlaskClient
import pytest
import sys
import os
from unittest.mock import patch, Mock
from flask import Flask
from dotenv import load_dotenv
from flask_mysqldb import MySQL

load_dotenv()

# Obtener la ruta del directorio raíz del proyecto
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(root_dir)
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_agregar_user(client):
    # Crear un objeto Mock para representar la conexión a la base de datos
    mock_database = Mock()

    # Crear una aplicación Flask para obtener un contexto de aplicación
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = os.getenv("DB_HOST")  
    app.config['MYSQL_USER'] = os.getenv("DB_USER")
    app.config['MYSQL_PASSWORD'] = os.getenv("DB_PASSWORD")
    app.config['MYSQL_DB'] = os.getenv("DB")
    app.config['MYSQL_CURSORCLASS'] = os.getenv("CURSOSRCLASS")
    MySQL(app)

    # Decorar la función de prueba para reemplazar la llamada real a la base de datos con el Mock
    with patch('flask_mysqldb.MySQL.connection', mock_database):
        # Configurar el comportamiento esperado del Mock (simular un resultado de la base de datos)
        mock_cursor = mock_database.cursor.return_value
        mock_cursor.fetchone.return_value = None  # Simula que no existe ningún usuario con el mismo email

        # Simular una solicitud POST con datos de registro
        response = client.post('/agregar', data=dict(
            name='John',
            last_name='Doe',
            email='john@example.com',
            password='password123'
        ), follow_redirects=True)

        # Verificar que la respuesta sea exitosa (código 200)
        assert response.status_code == 200

