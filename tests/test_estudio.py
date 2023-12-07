from flask.testing import FlaskClient
import pytest
from unittest.mock import patch, Mock
from flask import Flask
from dotenv import load_dotenv
from flask_mysqldb import MySQL

load_dotenv()

def test_estudio(client, mock_db):
    # Set up Flask session data
    with client.session_transaction() as session:
        session['name'] = 'John'
        session['last_name'] = 'Doe'
        session['email'] = 'john.doe@email.com'
        session['status'] = 'Tutor'
        session['nombre_grado'] = 'Ingenieria en Sistemas'
        session['photo_url'] = 'static/images/userPhoto.png',
        session['id_user'] = 1

    mock_cursor = mock_db.cursor.return_value
    mock_cursor.fetchall.return_value = [
        ('Title1', 'Subject1', 'Description1', 'Location1', 'Days1', 'Time1', 'Creator1'),
        ('Title2', 'Subject2', 'Description2', 'Location2', 'Days2', 'Time2', 'Creator2'),
        # Add more tuples as needed
    ]

    mock_cursor.fetchone.return_value = None

    # Simulate a POST request with event data
    response = client.post('/estudio', data=dict(
        title='Estudiar PROLOG',
        subject='Inteligencia Artificial',
        description='Estudiar PROLOG para el examen',
        location='Biblioteca',
        days='13/01/2024',
        time='12:00'
    ), follow_redirects=True)

    assert response.status_code == 200


def test_estudio_form_submission(client, mock_db):
    # Set up Flask session data
    with client.session_transaction() as session:
        session['name'] = 'John'
        session['last_name'] = 'Doe'
        session['email'] = 'john.doe@email.com'
        session['status'] = 'Tutor'
        session['nombre_grado'] = 'Ingenieria en Sistemas'
        session['photo_url'] = 'static/images/userPhoto.png',
        session['id_user'] = 1

    mock_cursor = mock_db.cursor.return_value
    mock_cursor.fetchall.return_value = []  # No existing study groups

    # Configure fetchone to return a dictionary-like object
    mock_cursor.fetchone.return_value = {'conteo': 0}

    response = client.post('/estudio', data=dict(
        title='Estudiar PROLOG',
        subject='Inteligencia Artificial',
        description='Estudiar PROLOG para el examen',
        location='Biblioteca',
        days='13/01/2024',
        time='12:00'
    ), follow_redirects=True)

    assert response.status_code == 200


