# conftest.py

import pytest
import os
import sys
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
