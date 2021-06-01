from application import db

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    units = db.Column(db.String(50))
    effect = db.Column(db.String(50))
    date_generated = db.Column(db.DateTime)
    def __repr__(self):
        return f"{self.name}: {self.units} units experience {self.effect}"
