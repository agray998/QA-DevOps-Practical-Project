from application import db

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(50))
    unit_type = db.Column(db.String(50))
    status_effect = db.Column(db.String(50))
    date_generated = db.Column(db.DateTime)
    def __repr__(self):
        return f"{self.name}: {self.units} units experience {self.effect}"
