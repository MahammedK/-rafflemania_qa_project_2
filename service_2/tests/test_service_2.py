from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from application import app
from application.routes import raffleletters

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_letters(self):
        with patch('requests.get') as g:
            g.return_value.text = "A"

            response = self.client.get(url_for('letters'))
            self.assertEqual(response.status_code, 200)