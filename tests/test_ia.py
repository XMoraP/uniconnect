from flask.testing import FlaskClient
import pytest
import sys
import os
from unittest.mock import patch
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

@patch('app.get_openai_response')
def test_chat(mock_openai_response, client: FlaskClient):
    mock_openai_response.return_value = "Mocked response from OpenAI"

    data = {'msg': 'Hola, estoy probando'}
    response = client.post('/get', data=data)

    mock_openai_response.assert_called_once()
    assert response.status_code == 200
    assert b'Mocked response from OpenAI' in response.data

def test_welcome_message(client):
    data = {'name': 'John'}
    response = client.post('/get_welcome_message', data=data)

    assert response.status_code == 200
    assert 'Bienvenido,' in response.data.decode('utf-8')
    assert '¿En qué puedo ayudarte?' in response.data.decode('utf-8')

def test_empty_message(client):
    data = {'msg': ''}
    response = client.post('/get', data=data)
    assert response.status_code == 400  




