from datetime import datetime
from app import db


class btc_mxn(db.Model):
    last = db.Column(db.String(20),  nullable=False)
    volume = db.Column(db.String(120),  nullable=False)
    created_at = db.Column(db.String(20), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return f"btc_mxn('{self.last}', '{self.volume}', '{self.created_at}')"

