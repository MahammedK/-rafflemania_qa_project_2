from unittest.mock import patch
from flask import url_for, Response
from flask_testing import TestCase
from requests_mock import mock
import requests_mock
from application import app, routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_secondround(self):
        raffle_letters = 'A'
        get_prizes = 'Mouthwash'
        response = self.client.post(url_for('secondround'), json = {'Letters': raffle_letters, 'Prizes': get_prizes})
        self.assertEqual(response.status_code, 200)

    def test_secondround_2(self):
        raffle_letters = 'B'
        get_prizes = 'Day at 10 Downing Street'
        response = self.client.post(url_for('secondround'), json = {'Letters': raffle_letters, 'Prizes': get_prizes})
        self.assertEqual(response.status_code, 200)

    def test_secondround_3(self):
        raffle_letters = 'U'
        get_prizes = 'A CheeseString'
        response = self.client.post(url_for('secondround'), json = {'Letters': raffle_letters, 'Prizes': get_prizes})
        self.assertEqual(response.status_code, 200)

    def test_secondround_4(self):
        raffle_letters = 'M'
        get_prizes = 'A Toilet Roll'
        response = self.client.post(url_for('secondround'), json = {'Letters': raffle_letters, 'Prizes': get_prizes})
        self.assertEqual(response.status_code, 200)

