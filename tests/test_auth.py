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

@pytest.fixture
def mock_db():
    # Create a mock for the database connection
    mock_database = Mock()

    # Create a Flask app for obtaining an application context
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = os.getenv("DB_HOST")  
    app.config['MYSQL_USER'] = os.getenv("DB_USER")
    app.config['MYSQL_PASSWORD'] = os.getenv("DB_PASSWORD")
    app.config['MYSQL_DB'] = os.getenv("DB")
    app.config['MYSQL_CURSORCLASS'] = os.getenv("CURSOSRCLASS")
    MySQL(app)

    # Decorate the function with patch to replace the real database connection with the mock
    with patch('flask_mysqldb.MySQL.connection', mock_database):
        yield mock_database

def test_agregar_user(client, mock_db):
    # Configure the expected behavior of the mock (simulate a database result)
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.fetchone.return_value = None  # Simulate that there is no user with the same email

    # Simulate a POST request with registration data
    response = client.post('/agregar', data=dict(
        name='John',
        last_name='Doe',
        email='john@example.com',
        password='password123'
    ), follow_redirects=True)

    # Verify that the response is successful (status code 200)
    assert response.status_code == 200
    # Add more assertions based on your specific requirements

