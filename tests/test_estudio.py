import json
import pytest
from unittest.mock import patch, Mock
from flask import Flask
from dotenv import load_dotenv
from flask_mysqldb import MySQL

load_dotenv()

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

    # Mock database cursor and set expectations
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.fetchall.return_value = []  # No existing study groups

    # Configure fetchone to return a dictionary-like object
    mock_cursor.fetchone.return_value = {'conteo': 0}

    # Simulate form submission
    response = client.post('/estudio', data=dict(
        title='Estudiar PROLOG',
        subject='Inteligencia Artificial',
        description='Estudiar PROLOG para el examen',
        location='Biblioteca',
        days='13/01/2024',
        time='12:00'
    ), follow_redirects=True)

    # Assert the expected behavior
    assert response.status_code == 200
    # assert b'Group created successfully' in response.data



def test_estudio_form_validation(client, mock_db):
    # Set up Flask session data for an authenticated user
    with client.session_transaction() as session:
        session['name'] = 'John'
        session['last_name'] = 'Doe'
        session['email'] = 'john.doe@email.com'
        session['status'] = 'Tutor'
        session['nombre_grado'] = 'Ingenieria en Sistemas'
        session['photo_url'] = 'static/images/userPhoto.png',
        session['id_user'] = 1

    # Mock database cursor and set expectations for an empty study_groups table
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.fetchall.return_value = []  # No existing study groups

    # Configure fetchone to return a dictionary-like object
    mock_cursor.fetchone.return_value = {'conteo': 0}

    # Simulate form submission with missing required fields
    response = client.post('/estudio', data=dict(
        title='',  # Missing title
        subject='Inteligencia Artificial',
        description='Estudiar PROLOG para el examen',
        location='Biblioteca',
        days='13/01/2024',
        time='12:00'
    ), follow_redirects=True)


    assert response.status_code == 200
    # assert b'Field is required' in response.data