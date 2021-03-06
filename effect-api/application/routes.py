from application import app
from flask import Flask, request, Response

@app.route('/get_effect', methods = ['POST'])
def effect():
    event_data = request.get_json()
    event_name = event_data["Event"]
    unit_type = event_data["Unit"]
    stats = {"Ranged inf.": "Range", "Melee inf.": "Defense", "Ranged cav.": "Range", "Melee cav.": "Attack strength", "Mechanised": "Movement"}
    effects = {"Gold Rush": "+5", "Weapons Upgrade": "+10", "Bountiful Harvest": "+2"}
    effect = f"{effects[event_name]} to {stats[unit_type]}"
    return Response(effect, mimetype='text/plain')
