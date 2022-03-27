from application import app
import random

@app.get('/get_unit')
def unit():
    unit_type = random.choice(["Ranged inf.", "Melee inf.", "Ranged cav.", "Melee cav.", "Mechanised"])
    return unit_type
