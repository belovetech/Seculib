from datetime import datetime
from models.attackattempt import AttackAttempt
import uuid

class DDOSAttackManager:
   def __init__(self, db):
      self.db = db

   def add_attack_attempt(self, **kwargs):
      try:
         kwargs['id'] = str(uuid.uuid4())
         attack_attempt = AttackAttempt(**kwargs)
         self.db.session.add(attack_attempt)
         self.db.session.commit()
         return self.get_attack_attempt_by_id(kwargs['id'])
      except Exception as e:
         print("Add attack attempt error: ", e)
         self.db.session.rollback()
         return None


   def get_all_attack_attempts(self, **kwargs):
      try:
         page = kwargs.get('page', 1)
         limit = kwargs.get('limit', 10)
         attack_attempt_objs = []
         attack_attempts = self.db.session.query(AttackAttempt).limit(limit).offset((page - 1) * limit).all()
         for attack_attempt in attack_attempts:
            attack_attempt = attack_attempt.__dict__.copy()
            attack_attempt.pop('_sa_instance_state')
            attack_attempt_objs.append(attack_attempt)
         return attack_attempt_objs
      except Exception as e:
         print("Get attack attempts error: ", e)
         return attack_attempt_objs
