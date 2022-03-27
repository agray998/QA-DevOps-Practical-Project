from application import app
import random
from fastapi.responses import PlainTextResponse

@app.get('/get_name', response_class = PlainTextResponse)
def name():
    event_name = random.choice(["Bountiful Harvest", "Gold Rush", "Weapons Upgrade"])
    return event_name