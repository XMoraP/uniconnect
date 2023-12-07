from flask.testing import FlaskClient
import pytest
import sys
import os
from unittest.mock import patch, Mock
from flask import Flask
from dotenv import load_dotenv
from flask_mysqldb import MySQL

load_dotenv()

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

