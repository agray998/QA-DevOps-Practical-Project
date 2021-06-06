from application import app, db
from flask import Flask, request, render_template, url_for
from application.models import Events
import requests
from datetime import date


# home route
@app.route('/', methods = ['GET'])
def home():
    event_name = requests.get('http://event_generator_name-api:5000/get_name')
    unit_type = requests.get('http://event_generator_unit-api:5000/get_unit')
    effect = requests.post('http://event_generator_effect-api:5000/get_effect', json = {"Event": event_name.text, "Unit": unit_type.text})
    event = Events(event_name = event_name.text, unit_type = unit_type.text, status_effect = effect.text, date_generated = date.today())
    db.session.add(event)
    db.session.commit()
    past5 = Events.query.order_by(Events.id.desc()).limit(5).all()
    return render_template('index.html', event = event, past5 = past5)

@app.route('/history', methods=['GET'])
def history():
    events_history = Events.query.all()
    return render_template('history.html', events_history = events_history)

