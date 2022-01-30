from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__name__))
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://flask-user:p4ssw0rd@172.16.0.2/flask"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

# Modelo
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, name, surname, email, password) -> None:
        self.name = name
        self.surname = surname
        self.email = email
        self.password = self.set_password(bytes(password, 'UTF-8'))

    def set_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password, salt)
        return hashed


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        # fields = ('name', 'surname', 'email', 'password')
        model = User

    name = ma.auto_field()
    surname = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()

user_schema = UserSchema()
users_schema = UserSchema(many=True)

db.create_all()

# Rutas
@app.route('/users')
def index():
    users = User.query.all()
    return jsonify(users_schema.dump(users))

@app.route('/users', methods=['POST'])
def store():
    email = request.json['email']
    name = request.json['name']
    surname = request.json['surname']
    password = request.json['password']

    user = User(name, surname, email, password)
    db.session.add(user)
    db.session.commit()

    return user_schema.dump(user), 201

@app.route('/users/<int:user_id>')
def show(user_id):
    user = User.query.get(user_id)
    if user == None:
        return jsonify({"message": "Not found"}), 404
    return user_schema.dump(user)


if __name__ == "__main__":
    app.run(debug=True)
