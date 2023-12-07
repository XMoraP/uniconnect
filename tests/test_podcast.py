from datetime import datetime
from io import BytesIO
from flask.testing import FlaskClient
import pytest
import sys
import os
from unittest.mock import patch, Mock
from flask import Flask
from dotenv import load_dotenv
from flask_mysqldb import MySQL

import pytest

from app import app  # Asegúrate de importar tu aplicación Flask

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_subir_audio(client, mock_db):
    # Configura el comportamiento esperado del mock (simula un resultado de base de datos)
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.fetchone.return_value = {'name': 'usuario_de_prueba'}

    # Crea un archivo de audio de prueba
    audio_data = b'fake_audio_data'
    audio_file = BytesIO(audio_data)
    audio_file.filename = 'test_audio.wav'

    # Simula la petición POST con el archivo de audio y una descripción
    response = client.post('/subir_audio', data={
        'audio': (audio_file, 'test_audio.wav'),
        'description': 'Descripción de prueba'
    })

    # Verifica que la respuesta sea exitosa (código de estado 200)
    assert response.status_code == 200
    assert b'Audio subido exitosamente' in response.data

    # Agrega más aserciones según sea necesario para verificar el comportamiento específico de tu aplicación