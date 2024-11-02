from app import app
from database import db

db.init_app(app)

with app.app_context():
    db.create_all()
    print("Banco de dados inicializado com sucesso.")