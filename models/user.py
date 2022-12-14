from core.app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(32), unique=True, nullable=False)
  email = db.Column(db.String(64), unique=True, nullable=False)
  password = db.Column(db.String(128), unique=True, nullable=False)
  def __repr__(self):
    return '<User %r>' % self.username