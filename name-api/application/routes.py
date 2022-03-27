from application import app
import random

@app.get('/get_name')
def name():
    event_name = random.choice(["Bountiful Harvest", "Gold Rush", "Weapons Upgrade"])
    return event_name