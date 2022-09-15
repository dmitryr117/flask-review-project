from models.user import User
from core.app import db, bcrypt

def authenticate(email, password):
  user = User.query.filter_by(email=email).first()
  if user and bcrypt.check_password_hash(user.password, password):
    return user
      

def identity(payload):
  user_id = payload['identity']
  print("User Identity: ", user_id)
  return None #userid_table.get(user_id, None)