from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from application import app
from application.routes import raffle_prizes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_prizes(self):
        with patch('requests.get') as g:
            g.return_value.text = "PortaLoo"

            response = self.client.get(url_for('prizes'))
            self.assertEqual(response.status_code, 200)