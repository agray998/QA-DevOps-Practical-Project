from application import app
from application.models import Event

@app.post('/get_effect')
def effect(event: Event):
    event_name, unit_type = event.event, event.unit
    stats = {"Ranged inf.": "Range", "Melee inf.": "Defense", "Ranged cav.": "Range", "Melee cav.": "Attack strength", "Mechanised": "Movement"}
    effects = {"Gold Rush": "+5", "Weapons Upgrade": "+10", "Bountiful Harvest": "+2"}
    effect = f"{effects[event_name]} to {stats[unit_type]}"
    return effect
