from application import db

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(50))
    unit_type = db.Column(db.String(50))
    status_effect = db.Column(db.String(50))
    date_generated = db.Column(db.DateTime)
    def __str__(self):
        return f"{self.event_name}: {self.unit_type} units experience {self.status_effect}"
