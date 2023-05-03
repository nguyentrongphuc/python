from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:P%40ssw0rd@localhost:5432/snowflake' #The password contains "@", you can escape the "@" character using "%40" instead.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    
    def __repr__(self):
        return f'<Person Id: {self.id}, name:{self.name}>'

app.app_context().push()
# As of Flask-SQLAlchemy 3.0, all access to db.engine (and db.session) requires an active Flask application context. db.create_all uses db.engine, so it requires an app context.
# with app.app_context():
db.create_all()
    
@app.route('/')

def index():
    person = Person.query.first()
    return 'Hello ' + person.name
