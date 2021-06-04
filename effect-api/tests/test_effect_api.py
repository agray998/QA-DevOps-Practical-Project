from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
# import the app's classes and objects
from application import app
from application.routes.get_effect import get_effect

# Create the base class
class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):

    def test_get_effect(self):
        response = self.client.post(url_for('effect'), json={"Event": "Blindness", "Unit": "Ranged inf."})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'-5 to Range', response.data)