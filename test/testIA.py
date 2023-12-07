import unittest
from unittest.mock import patch
from flask import Flask, request, session
import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(root_dir)
from app import chat, get_openai_response

class TestOpenAIInteraction(unittest.TestCase):

    @patch('openai.ChatCompletion.create')
    def test_openai_api_interaction(self, mock_chat_completion):
        """
        Testea si la función get_openai_response maneja correctamente
        la respuesta esperada de OpenAI.
        """
        messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Hola, estoy probando'}]

        mock_chat_completion.return_value = {
            'choices': [{'message': {'content': 'Respuesta de OpenAI'}}]
        }

        response = get_openai_response(messages)

        mock_chat_completion.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=100,
        )
        self.assertEqual(response, 'Respuesta de OpenAI')

    @patch('openai.ChatCompletion.create')
    def test_openai_api_interaction_fail(self, mock_chat_completion):
        """
        Testea cómo la función get_openai_response reacciona ante 
        una respuesta diferente de la API de OpenAI.
        """
        messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Hola, estoy probando'}]

        mock_chat_completion.return_value = {
            'choices': [{'message': {'content': 'Respuesta diferente de OpenAI'}}]
        }

        response = get_openai_response(messages)

        mock_chat_completion.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=100,
        )

        self.assertNotEqual(response, 'Respuesta de OpenAI')
    
    @patch('openai.ChatCompletion.create')
    def test_openai_api_empty_response(self, mock_chat_completion):
    # Simula mensajes enviados a la API
        messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': 'Hola, estoy probando'}]

    # Define una respuesta simulada vacía de la API de OpenAI
        mock_chat_completion.return_value = {
        'choices': [{'message': {'content': ''}}]
    }

    # Llama a la función de manejo de OpenAI
        response = get_openai_response(messages)

    # Verifica si la función llamó a la API de OpenAI con los mensajes dados
        mock_chat_completion.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=100,
    )

    # Verifica si la función devuelve una respuesta vacía
        self.assertEqual(response, '')

if __name__ == '__main__':
    unittest.main()
