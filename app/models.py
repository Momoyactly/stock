from datetime import datetime
from app import db


class btc_mxn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last = db.Column(db.String(20), unique=True, nullable=False)
    volume = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"btc_mxn('{self.last}', '{self.volume}', '{self.created_at}')"

