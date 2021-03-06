from flask import url_for
from flask_testing import TestCase
from datetime import date
import requests_mock
import pytest
# import the app's classes and objects
from application import app, db
from application.models import Events

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                DEBUG=True,
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test event
        sample1 = Events(event_name="Bountiful Harvest", unit_type="Ranged inf.", status_effect="+2 to Range", date_generated=date(2021, 6, 3))

        # save event to database
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
  
    def test_home_get(self):
        # mock values
        name = "Gold Rush"
        unit = "Melee cav."
        effect = "+10 to Attack strength"
        with requests_mock.Mocker() as m:
            m.get("http://event_generator_name-api:5000/get_name", text=name)
            m.get("http://event_generator_unit-api:5000/get_unit", text=unit)
            m.post("http://event_generator_effect-api:5000/get_effect", text=effect)
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Bountiful Harvest', response.data)
            self.assertIn(b'Gold Rush', response.data)

    def test_hist_get(self):
        response = self.client.get(url_for('history'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bountiful Harvest', response.data)