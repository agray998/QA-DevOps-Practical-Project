from application import app
from flask import Flask, request, Response
import random

@app.route('/get_unit', methods=['GET'])
def unit():
    unit_type = random.choice(["Ranged inf.", "Melee inf.", "Ranged cav.", "Melee cav.", "Mechanised"])
    return Response(unit_type, mimetype='text/plain')
