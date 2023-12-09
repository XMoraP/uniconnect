from flask.testing import FlaskClient
import pytest
from unittest.mock import patch, Mock
from flask import Flask, session
from dotenv import load_dotenv
from flask_mysqldb import MySQL
import io
import base64
from PIL import Image

load_dotenv()

def test_subir_imagen(client, mock_db):
    # Simular una sesión iniciada
    with client.session_transaction() as sess:
        sess['id_user'] = 1  # Establecer el ID de usuario en la sesión

    # Crear una imagen de prueba
    test_image = Image.new('RGB', (100, 100))
    image_io = io.BytesIO()
    test_image.save(image_io, 'JPEG')
    image_io.seek(0)

    # Simular la solicitud POST con la imagen
    response = client.post('/subir_imagen', data={'imagen': (image_io, 'test.jpg')}, content_type='multipart/form-data')

    # Verificar el código de estado de la respuesta
    assert response.status_code == 302  # Verificar que se redirige correctamente

    # Verificar que se establece el mensaje en la sesión
    with client.session_transaction() as sess:
        assert sess['mensaje']['tipo'] == 'successUpdate'
        assert sess['mensaje']['contenido'] == 'imagen actualizada'

def test_cargar_imagen(client, mock_db):
    # Simular una sesión iniciada
    with client.session_transaction() as sess:
        sess['id_user'] = 1  # Establecer el ID de usuario en la sesión

    # Simular la respuesta de la base de datos para una imagen existente
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.fetchone.return_value = {'image': base64.b64encode(b'test_image_data').decode('utf-8')}

    # Realizar una solicitud GET al endpoint '/cargar_imagen'
    response = client.get('/cargar_imagen')

    # Verificar el código de estado de la respuesta
    assert response.status_code == 200

    # Verificar que se recibe una imagen como respuesta
    assert response.mimetype.startswith('image/')






    

