from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class stress(db.Model):
    __tablename__ = 'stress'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    stress_level = db.Column(db.Integer)
    stress_date = db.Column(db.DateTime)

    def __init__(self, user_id, stress_level, stress_date):
        self.user_id = user_id
        self.stress_level = stress_level
        self.stress_date = stress_date

class sleep(db.Model):
    __tablename__ = 'sleep'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    sleep_level = db.Column(db.Integer)
    sleep_date = db.Column(db.DateTime)

    def __init__(self, user_id, sleep_level, sleep_date):
        self.user_id = user_id
        self.sleep_level = sleep_level
        self.sleep_date = sleep_date