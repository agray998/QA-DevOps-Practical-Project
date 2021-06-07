from application import app
from flask import Flask, request, Response
import random

@app.route('/get_name', methods=['GET'])
def name():
    event_name = random.choice(["Bountiful Harvest", "Gold Rush", "Weapons Upgrade"])
    return Response(event_name, mimetype='text/plain')