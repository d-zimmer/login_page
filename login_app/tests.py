# login_app/tests.py
import requests
from django.test import TestCase

class APITestCase(TestCase):
    def test_api_login(self):
        url_api_login = 'http://127.0.0.1:8000/api/login/'
        data = {'username': 'admin', 'password': 'admin'}
        response = requests.post(url_api_login, data=data)
        self.assertEqual(response.status_code, 200)  # ou qualquer verificação que você precise
