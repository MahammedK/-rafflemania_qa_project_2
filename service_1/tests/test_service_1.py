from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from requests_mock import mock
import requests_mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_draw(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/letters', text='U')
            m.get('http://service_3:5000/prizes', text='PortaLoo')
            m.post('http://service_4:5000/secondround', text='AirPods')

            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)

class TestResponse_2(TestBase):
    def test_draw_2(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/letters', text='B')
            m.get('http://service_3:5000/prizes', text='Sparkling Water')
            m.post('http://service_4:5000/secondround', text='QA CloudAcademy free demo')

            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)

class TestResponse_3(TestBase):
    def test_draw_3(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/letters', text='I')
            m.get('http://service_3:5000/prizes', text='A Can of Tuna')
            m.post('http://service_4:5000/secondround', text='AirPods')

            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)

class TestResponse_4(TestBase):
    def test_draw_4(self):
        with requests_mock.Mocker() as m:
            m.get('http://service_2:5000/letters', text='M')
            m.get('http://service_3:5000/prizes', text='A CheeseString')
            m.post('http://service_4:5000/secondround', text='AirPods')

            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)