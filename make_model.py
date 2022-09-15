from core.app import db, create_app

print("Creating database tables:")
app = create_app()
with app.app_context():
  db.create_all()