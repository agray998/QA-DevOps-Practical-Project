from application import app
import random
from fastapi.responses import PlainTextResponse

@app.get('/get_unit', response_class = PlainTextResponse)
def name():
    unit_class = random.choice(["Ranged inf.", "Melee inf.", "Ranged cav.", "Melee cav.", "Mechanised"])
    return unit_class