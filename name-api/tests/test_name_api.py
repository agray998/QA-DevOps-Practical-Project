from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
# import the app's classes and objects
from application import app
from application.routes.get_name import get_name

# Create the base class
class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):

    def test_get_name(self):
       with patch('random.choice') as r:
           r.return_value = "Ill omen"
           response = self.client.get(url_for('name'))
           self.assertEqual(response.status_code, 200)
           self.assertIn(b'Ill omen', response.data)