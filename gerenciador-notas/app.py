#Configuração do app Flask.

from flask import Flask
from routes import configure_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)