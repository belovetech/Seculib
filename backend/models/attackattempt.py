from models.engine.db import db

class DDOSAttackAttempt(db.Model):
    __tablename__ = 'ddos_attack_attempts'

    id = db.Column(db.String(25), primary_key=True)
    ip_address = db.Column(db.String(25), nullable=False)
    user_agent = db.Column(db.String(200))
    request_url = db.Column(db.String(200))
    request_count = db.Column(db.Integer, nullable=False)
    attempt_date = db.Column(db.DateTime, nullable=False)
    attack_type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<DDOSAttackAttempt {self.ip_address}>'

    def __str__(self):
        return f'{self.ip_address} - {self.attack_type}'
